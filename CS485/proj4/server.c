/* $begin serve:rimain */
#include "csapp.h"
#include "sys/types.h"

char *userpass[2][128];
char *execcom[128];

void readconfig();
void readcommand();

int main(int argc, char **argv) 
{
    int listenfd, connfd, port;
    socklen_t clientlen;
    struct sockaddr_in clientaddr;
    struct hostent *hp;
    char *haddrp;
    if (argc != 2) {
	fprintf(stderr, "usage: %s <port>\n", argv[0]);
	exit(0);
    }
    port = atoi(argv[1]);


    // read in the first line from the client
    readconfig();
    readcommand();

    //size_t n;
    char buf[128];
    char user[40];
    char pass[40];
    rio_t rio;

    listenfd = Open_listenfd(port);

    clientlen = sizeof(clientaddr);
    connfd = Accept(listenfd, (SA *)&clientaddr, &clientlen);

    Rio_readinitb(&rio, connfd);
   
    //read username and password from client. Each individual line.
    Rio_readlineb(&rio, user, 40); //line:netp:echo:eof
    Rio_readlineb(&rio, pass, 40);
	

    int login = 0;
    int ctr = 0;

    strtok(pass, "\n");
    strtok(user, "\n");
    while(ctr < 128)
    {
	 if(strcmp(userpass[0][ctr], user) == 0 && (strcmp(userpass[1][ctr], pass)) == 0)
	 {
			login++;
	 }
	 ctr++;
    }
    
    if (login == 0)
    {
	printf("User %s Failed logging in\n", user);
	Rio_writen(connfd, "Login Failed\n", 14);
	Close(connfd);
	exit(0);
    }
    else
    {
	 // Determine the domain name and IP address of the client 
        hp = Gethostbyaddr((const char *)&clientaddr.sin_addr.s_addr,
                           sizeof(clientaddr.sin_addr.s_addr), AF_INET);
        haddrp = inet_ntoa(clientaddr.sin_addr);
        printf("server connected to %s (%s)\n", hp->h_name, haddrp);
	
	printf("User %s logging in from %s at TCP Port %d\n", user, haddrp, port);
	printf("User %s successfully logged in.\n", user);
	Rio_writen(connfd, "Login Successful\n", 17);//Warning if this isn't 17 it will affect every Rio_writen after this
    
	ctr = 0;
    	while(ctr == 0)
    	{
    		//reads your command from the client
    		Rio_readlineb(&rio, buf, 128);
		strtok(buf, "\n");
		printf("User %s sent the commandline %s to be executed\n", user, buf);

		if(strcmp(buf, "quit") == 0)
		{
			printf("Logged out\n");
			Rio_writen(connfd, "quit\n", 5);// Same warning as above
			ctr++;
		}
		else
		{
			 char *file;
			 char *command;
			 char *thirdinput;
			 char *str = buf;            //buf = /bin/cat echo.c                                     

                         command = strtok(str, " "); //command = /bin/cat
                         file = strtok(NULL, " ");   //file = echo.c
			 thirdinput = strtok(NULL, " ");

			 int usecommand = 0;
			 int ctr2 = 0;
			 while(ctr2 < 128)
		         {
         			if(strcmp(execcom[ctr2], command) == 0)
         		 	{
                        		usecommand++;
         		 	}
         			ctr2++;
    			 }
			

			if(usecommand == 0)
			{
				Rio_writen(connfd, "nocomm\n", 7);// Same warning as above
				printf("Cannot execute '%s' on this server.\n", buf);
			}
			else
			{
				printf("Forking/Execing the command '%s' on behalf of %s\n", buf, user);
				
				char buffer[MAXLINE];
				int pipefd[2];
				pipe(pipefd);				

				pid_t pid = fork();
                                if (!pid)
				{
					close(pipefd[0]);
					
					dup2(pipefd[1], 1);
					dup2(pipefd[1], 2);

					close(pipefd[1]);

                                        char *env[] = {0};
					char *arg[] = {command, file, thirdinput, NULL};			
		
                                        //call your executable in your current directory
					execve(command, arg, env);
                                }
                                else if (pid == -1)
                                {
                                        perror("fork");
                                }
				else
				{
					//parent
					close(pipefd[1]);
					while (read(pipefd[0], buffer, sizeof(buffer)) != 0)
    					{
    					}
				}


                                        int status;
                                        wait(&status);

				//sends out the string results of exec.
				Rio_writen(connfd, buffer, strlen(buffer));
			
				//we use this as a counter to tell the client that we have sent everything over.
				Rio_writen(connfd, "exec\n", 5);// Same warning as above
				
				int ctr2 = 0;
				while(ctr2 < MAXLINE)
				{
					buffer[ctr2] = 0;
					ctr2++;
				}
			}
			

		}
    	}
    }

    Close(connfd);
    exit(0);
}

void readconfig()
{
	// Allocate userpass char array
	int i;
	int j;
        for(i=0; i<2; i++ ){
                for(j=0; j<128; j++){
                        userpass[i][j] = malloc(40);
                }
         }

        FILE *file;
	char line[128];
	int c = 0;
	char *username;
	char *password;

        file = fopen("rrshusers.txt", "r");
        if (file) 
	{
                while (Fgets(line, sizeof(line), file) != NULL)
		{
			char *str = line;
			username = strtok(str, " ");
			password = strtok(NULL, " ");			

			strtok(password, "\n");
			strcpy(userpass[0][c], username);
			strcpy(userpass[1][c], password);	
			c++;
                }
                fclose(file);
        }

}

void readcommand()
{
        // Allocate userpass char array
        int i;
        for(i = 0; i < 128; i++)
	{
            execcom[i] = malloc(128);
                
        }

        FILE *file;
        char line[128];
        i = 0;

        file = fopen("rrshcommands.txt", "r");
        if (file)
        {
                while (Fgets(line, sizeof(line), file) != NULL)
                {
			strtok(line, "\n");
                        strcpy(execcom[i], line);
                        i++;
                }
                fclose(file);
        }

}


/* $end serverimain */
