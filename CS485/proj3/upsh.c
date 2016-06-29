/* $begin shellmain */
#include "csapp.h"
#include  <stdlib.h>
#include  <signal.h>
#include  <stdio.h>
#include  <signal.h>
#include  <sys/types.h> // 
#include  <sys/wait.h>  //so we can use waitpid and status
#include  <dlfcn.h>  // allows us to use dlopen, dlclose, dlsym
#define MAXARGS   128

struct NewBuiltIn{
        char CommandName[64];
        char FunctionName[64];
        char AnalyzerName[64];
};

struct NewBuiltIn pluggin_method;

char cmdnames[128][128];
char funcnames[128][128];
char analyzenames[128][128];
char filename[128][128];

pid_t PIDS[128];

int out, in, inpos, outpos;

char prompt[MAXARGS] = "upsh> ";

/* function prototypes */
void eval(char *cmdline);
int parseline(char *buf, char **argv);
int p3parseline(char *buf, char **argv); /* new parseline function for cs485 project 3 */
int builtin_command(char **argv);
void PIDadjust(int spot); //adjusts PIDS array if a PID is finished
void reaperthegrim(); //signal handler
char* analyzerfunc(char *cmdline); //runs analyzer function from pluggins
int outdirection(char **argv); // Handles output redirection, signaled from parseline
int  indirection(char **argv); // Handles input redirection, signaled from parseline


int main() 
{
    //makes an array of straight 0's
    int i;
    for(i = 0; i < 128; i++)
    {
	PIDS[i]=0;
    }

    char cmdline[MAXLINE]; /* Command line */
    char* analyzeret;

    int outcommand = dup(STDOUT_FILENO);
    int incommand = dup(STDIN_FILENO);
   
    while (1) {
	/* Read */
	printf("%s", prompt);
	fgets(cmdline, MAXLINE, stdin); 
	analyzeret = analyzerfunc(cmdline); //(in the .so) returns pointer to character string which is passed to eval
	if (feof(stdin)) //catches the ctrl-d. EOF represents it. so we use feof() to check.
	    {   printf("\n");
		exit(0);}

	/* Evaluate */
	eval(analyzeret);
	dup2(outcommand, STDOUT_FILENO);
    dup2(incommand, STDIN_FILENO);

    } 
}
/* $end shellmain */
  
/* $begin eval */
/* eval - Evaluate a command line */
void eval(char *cmdline) 
{

    char *argv[MAXARGS]; /* Argument list execve() */
    char buf[MAXLINE];   /* Holds modified command line */
    int bg;              /* Should the job run in bg or fg? */
    pid_t pid;           /* Process id */

    signal(SIGCHLD, reaperthegrim);
    strcpy(buf, cmdline);
        bg = parseline(buf, argv);  
    //bg = p3parseline(buf, argv); /* call new parseline function for cs485 project 3 */
    if (argv[0] == NULL)  
	return;   /* Ignore empty lines */
    
    if (!builtin_command(argv)) { 
	if ((pid = fork()) == 0) {   /* Child runs user job */
	    if (execve(argv[0], argv, environ) < 0) {
		printf("%s: Command not found.\n", argv[0]);
		exit(0);
	    }
	}

	/* Parent waits for foreground job to terminate */
	if (!bg) {
	    int status;
	    if (waitpid(pid, &status, 0) < 0)
		unix_error("waitfg: waitpid error");
	}
	else{
	    printf("%d %s", pid, cmdline);
	    int i =0;
	    int ctr = 1;
	    while(ctr==1)
                {
			//puts the pid into the PIDS array so we can keep track of all pids
                        if(PIDS[i]==0)
                        {
                                PIDS[i]=pid;
                                ctr=0;
			}
                        else
                        {
                                i++;
                        }
                }
	   }
         }

    in = 0;
    out = 0;
    inpos = 0;
    outpos = 0;
    
    return;
}

/* If first arg is a builtin command, run it and return true */
int builtin_command(char **argv) 
{
	if (out == 1){
        outdirection(argv);
        }
    if (in == 1){
        indirection(argv);
        }
    if (!strcmp(argv[0], "quit")) /* quit command */
	exit(0);  
    if (!strcmp(argv[0], "&"))    /* Ignore singleton & */
	return 1;
    if (!strcmp(argv[0], "culater")) /* culater command */
        exit(0);
    if (!strcmp(argv[0], "%")) /* % command */
        return 1;
    if (!strcmp(argv[0], "setprompt")) /* setprompt command ex: 'setprompt "my shell > "' */
        {
		strcpy(prompt, argv[1]);
		return 1;
	}
     if (!strcmp(argv[0], "fg")) /* fg command */
	{

		int i = atoi(argv[1]);

		if(!argv[1])
		{
			printf("You need a job number\n");
			return 1;
		}		
		else if(PIDS[i-1] != 0)
		{
			int status;
			waitpid(PIDS[i-1], &status, 0);
			PIDadjust(i-1);
		}
		else
		{
			printf("fg command must include a valid job number\n");
		}
		return 1;
	}
     if (!strcmp(argv[0], "bgjobs")) //prints all your background jobs in a list with a number
	{

		int i = 0;
		int ctr=1;
		while(ctr==1)
		     {
			 if(PIDS[i]==0)
                        	{
					ctr=0;
                        	}
                        	else
   	                     	{
					printf(" [%d] ",i+1);

					pid_t pid = fork();
					if (!pid){
						
						char str[40];
						sprintf(str, "/proc/%d/cmdline", PIDS[i]);
						

                				char *env[] = {0};
                				char *arg[] ={"/bin/cat", str, NULL};

                				//call your executable in your current directory
                				execve("/bin/cat", arg, env);
        			        }
        				else if (pid == -1)
        				{
                				perror("fork");
        				}


        				int status;
        				wait(&status);
					printf("\n");

					i++;
                        	}
		     }
 
		return 1;
	}
     if (!strcmp(argv[0], "cd")) // changes your directory
	{
		 //Check to see if any arguments are passed to cd
                if (!argv[1]) {
                        fprintf(stderr, "expected argument to \"cd\"\n");
                }
                //If there are any arguments, change the directory
                else {
                        if(chdir(argv[1]) != 0) {
                                perror("upsh>");
                        }
                }

                return 1;


	}
     if (!strcmp(argv[0], "loadpluggin")) // loads a .so file pluggin
	{

		void *handle;
		struct NewBuiltIn *pluggin;
		char *error;

		//opens the .so file
		handle = dlopen (argv[1], RTLD_LAZY);
		if (!handle)
		{
			fputs(dlerror(), stderr);
			printf("\n");
			return 1;
		}
		
		//pulls struct NewBuiltIn pluggin_method from .so
		pluggin = dlsym(handle, "pluggin_method");
		if ((error = dlerror()) != NULL)
                {
                        fputs(error, stderr);
                        printf("\n");
                        return 1;
                }

		//insert the pluggin info into an array so we can have mult pluggins.
		int ctr = 0;
		int i = 0;
		while(ctr == 0)
		{
			if(!cmdnames[i][0])
			{
				strcpy(filename[i], argv[1]);
				strcpy(cmdnames[i], pluggin->CommandName);
				strcpy(funcnames[i], pluggin->FunctionName);
				strcpy(analyzenames[i], pluggin->AnalyzerName);
				ctr++;
			}
			else
			{
				i++;
			}

		}
		
		dlclose(handle);

		return 1;
		
	}

	// checks all of the new built in commands
	int ctr = 0;
	int i = 0;
	while(ctr == 0)
	{ 
		if (!cmdnames[i] || i == 128) //if it ends cmdnames or goes through entire array the loop ends.
		{
			ctr++;
		}
		else if (!strcmp(argv[0], cmdnames[i])) // newbultin command 
		{

			void *handle;
                	int  (*mysofunc)(char**);
                	char *error;

			//opens .so file associated with the commandname
                	handle = dlopen (filename[i], RTLD_LAZY);
                	if (!handle)
                	{
                        	fputs(dlerror(), stderr);
                        	printf("\n");
                        	return 1;
                	}

			//pulls out the function for the .so with same command name
                	mysofunc = dlsym(handle, funcnames[i]);
                	if ((error = dlerror()) != NULL)
                	{
                        	fputs(error, stderr);
                        	printf("\n");
                        	return 1;
	                }

			//calls the .so function
			 (*mysofunc)(argv);
			dlclose(handle);
			return 1;
		}
		else
		{
			//increments so we can check the next cmdname in the array and see if it matches argv[0]
			i++;
		}
	}

    return 0;                     /* Not a builtin command */
}
/* $end eval */

/* $begin parseline */
/* parseline - Parse the command line and build the argv array */
int parseline(char *buf, char **argv) 
{
    char *delim;         /* Points to first space delimiter */
    int argc;            /* Number of args */
    int bg;              /* Background job? */

    buf[strlen(buf)-1] = ' ';  /* Replace trailing '\n' with space */
    while (*buf && (*buf == ' ')) /* Ignore leading spaces */
	buf++;

    /* Build the argv list */
    argc = 0;
    while ((delim = strchr(buf, ' '))) {
	argv[argc++] = buf;
	*delim = '\0';
	buf = delim + 1;
	while (*buf && (*buf == ' ')) /* Ignore spaces */
	       buf++;
    }
    argv[argc] = NULL;
    
    if (argc == 0)  /* Ignore blank line */
	return 1;

	/* Check for special chars */

    int i;
    for(i=0; i < argc-1; i++){

        if(*argv[i] == '<'){ /* If Infile indicator exists */
                in = 1;
                inpos = i;
        }

        if(*argv[i] == '>'){ /* If Outfile indicator exists */
                out = 1;
                outpos = i;
        }
    }


    /* Should the job run in the background?
	basically if you do /bin/sleep 100 & it works in the background 
    */
    if ((bg = (*argv[argc-1] == '&')) != 0)
	argv[--argc] = NULL;

    return bg;
}
/* $end parseline */

// Handles output redirection, signaled from parseline
int outdirection(char **argv){
        int output = open(argv[outpos+1], O_WRONLY | O_TRUNC | O_CREAT, S_IRUSR | S_IRGRP | S_IWGRP | S_IWUSR);
        /* Output placed in Output File rather than the console  */
        dup2(output, STDOUT_FILENO);
        close(output); /* Close File */

        argv[outpos] = NULL;
        argv[outpos+1] = NULL;

        return 1;
}

// Handles input redirection, signaled from parseline
int indirection(char **argv){
        int input = open(argv[inpos+1], O_RDONLY);
        /* Input redirected to function rather than console  */
        dup2(input, STDIN_FILENO);
        close(input); /* Close File */

        argv[inpos] = NULL;
        argv[inpos+1] = NULL;

        return 1;
}


// function that changes the array because a PID was killed and reaped.
void PIDadjust(int spot)
{
	int ctr = 0;
	int i = 1;
	int i2 = 0;
	
	while(ctr==0)
	{
		if(PIDS[spot + i]!=0)
		{
			PIDS[spot + i2] = PIDS[spot + i];
		}
		else
		{
			PIDS[spot + i2] = 0;
			ctr++;
		}
		
		i++;
		i2++;

	}


}

//if a PID ends, this is the signal handler to kill and reap it.
void reaperthegrim()
{
	union wait wstat;
	
	while(1)
	{
		pid_t pid = wait3 (&wstat, WNOHANG, (struct rusage *)NULL );
		if (pid == 0)
			return;
		else if (pid == -1)
			return;
		else
		{
			printf ("Child %d terminated with exit status %d\n",pid, wstat.w_retcode);
			int i;
			for(i = 0; i < sizeof(PIDS); i++)
			{
					if (PIDS[i] == pid)
					{
						PIDadjust(i);
					}
			}

		}
	}
}

//runs the analyzer function from a .so file
char* analyzerfunc(char *cmdline)
{
	char* thereturn; 
	int ctr = 0;
	int i = 0;
	int ctr2 = 0;
	while(ctr == 0)
	       {
			if(i == 128)
			{
				ctr++;
			}
			else if (!analyzenames[i][0] || !analyzenames[i][1])
                	{
                        	i++;
                	}
			else
	       		{


				void *handle;
                        	char*  (*mysofunc)(char*);
                        	char *error;

       		                handle = dlopen (filename[i], RTLD_LAZY);
                        	if (!handle)
                        	{
                                	fputs(dlerror(), stderr);
                                	printf("\n");
                                	return thereturn;
                        	}
                
                        	mysofunc = dlsym(handle, analyzenames[i]);
                        	if ((error = dlerror()) != NULL)
                        	{	
                                	fputs(error, stderr);
                                	printf("\n");
                                	return thereturn;
                        	}
			
				//if it is the first analyzer function called it uses cmdline else use thereturn from 1st call.
				if(ctr2 == 0)
				{ 
                        		thereturn =  (*mysofunc)(cmdline);
					ctr2++;
                        	}
				else
				{
					thereturn = (*mysofunc)(thereturn);
					ctr2++;
				}
				dlclose(handle);
				i++;
			}

		}

		if (ctr2 != 0)
		{
			return thereturn;
		}
		else
		{
			return cmdline;
		}
}



