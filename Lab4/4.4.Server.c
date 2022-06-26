#include <stdio.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#define MAX 200

//Function designed for chat between client and server
void func(int connfd)
{
	char buff[MAX];
	int n;

	//Infinite loop for chat
	for(;;)
    {
		bzero(buff, MAX);

		//Read the message from client and copy it in buffer
		read(connfd, buff, sizeof(buff));
		//Print buffer which contains the client contents
		printf("Client: %s", buff);
		printf("Server: ");
		bzero(buff, MAX);
		n = 0;
		//Copy server message in the buffer
		while((buff[n++] = getchar()) != '\n')
			;

		//Send that buffer to the client
		write(connfd, buff, sizeof(buff));

		//If msg contains "Exit" then server exit and chat ended.
		if(strncmp("exit", buff, 4) == 0)
        {
			printf("Server Exit...\n");
			break;
		}
	}
}

int main(){
	int sockfd, connfd, len;
	struct sockaddr_in server, client;

	//Socket create and verification
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if(sockfd == -1)
    {
		printf("socket creation failed...\n");
		exit(0);
	}
	else
		printf("Socket successfully created..\n");

	bzero(&server, sizeof(server));

	//Assign IP, PORT
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons(8888);

	//Bind
	if(bind(sockfd,(struct sockaddr*)&server, sizeof(server)) < 0)
    {
		puts("bind failed");
		exit(0);
	}
	else
		puts("Bind successful");

	//Listen
	if((listen(sockfd, 5)) != 0)
    {
		puts("Listen failed.");
		exit(0);
	}
	else
		puts("Server listening...");
	len = sizeof(client);

	//Accept the data packet from client
	connfd = accept(sockfd, (struct sockaddr*)&client, &len);
	if(connfd < 0)
    {
		puts("server accept failed");
		exit(0);
	}
	else
		puts("Client accepted.\n");

	//Function for chatting between client and server
	func(connfd);

	//After chatting close the socket
	close(sockfd);
}