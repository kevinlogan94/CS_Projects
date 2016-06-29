/*
 * client.c - A client
 */
/* $begin clientmain */
#include "csapp.h"

int main(int argc, char **argv) 
{
    int clientfd, port;
    char *host, buf[128],user[40], pass[40], command[128], finish[MAXLINE];
    rio_t rio;

    if (argc != 3) {
	fprintf(stderr, "usage: %s <host> <port>\n", argv[0]);
	exit(0);
    }
   
    
    printf("Username: ");
    Fgets(user, 40, stdin);
  
    printf("Password: ");
    Fgets(pass, 40, stdin);

    host = argv[1];
    port = atoi(argv[2]);

    clientfd = Open_clientfd(host, port);
    Rio_readinitb(&rio, clientfd);
    
    //write to the server the username and pass
    Rio_writen(clientfd, user, strlen(user));
    Rio_writen(clientfd, pass, strlen(pass));

    //read whether the user and pass was a success
    Rio_readlineb(&rio, buf, 128);

    printf("%s", buf);

    int ctr = 0;
    if(strcmp(buf, "Login Successful\n") == 0)
    {
	while(ctr == 0)
	{
		printf("rrsh > ");
		Fgets(command, 128, stdin);
                        
		//sends your command to the server
                Rio_writen(clientfd, command, strlen(command));
                //reads in the program finisher command
                Rio_readlineb(&rio, finish, MAXLINE);

		//if the command isn't allowed
		strtok(command, "\n");
                        
		if(strcmp(finish, "nocomm\n") == 0)
                {
                        printf("The command '%s' is not allowed.\n", command);
                }
		else if(strcmp(finish, "quit\n") == 0)
 	        {
             	        printf("Logged out\n");
                       	ctr++;
                }
		else
		{
			int ctr = 0;
			while(ctr == 0)
			{
				//prints the line generated from exec on the server.
				printf("%s", finish);
			
				//Gets us the next line generated from exec on the server.
				Rio_readlineb(&rio, finish, MAXLINE);
				if(strcmp(finish, "exec\n") == 0)
				{
					ctr++;
				}
			}
		}

	}
    }
   
    Close(clientfd); //line:netp:client:close
    exit(0);
}
/* $end clientmain */
