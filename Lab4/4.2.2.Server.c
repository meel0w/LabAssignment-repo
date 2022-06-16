#include<stdio.h>
#include<sys/socket.h>
#include<arpa/inet.h> //inet_addr
#include<string.h>
#include<unistd.h>

int main(int argc, char *argv[])
{
	int socket_desc , new_socket, c, client_sock, read_size;
	struct sockaddr_in server, client;
	char *message, client_reply[2000];

	// Create socket
	socket_desc = socket (AF_INET, SOCK_STREAM , 0);
	
	if (socket_desc == -1)
	{
		printf("Could not create socket");
	}

	//Prepare the sockaddr_in structure
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port=htons( 8888);

	//Bind
	if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) <0)
	{
		puts("bind failed");
	}

	puts("bind done");

	// Listen
	listen(socket_desc, 3);

    //Accept and incoming connection
    puts("Waiting for incoming connections...");
    c = sizeof(struct sockaddr_in);

	//accept connection from an incoming client
    while( (new_socket = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c)) )
	{
		puts("Connection accepted");
	
	    //Receive a message from client
        while( (read_size = recv(new_socket , client_reply , 2000 , 0)) > 0 )
        {
            //Send the message back to client
            write(new_socket , client_reply , strlen(client_reply));
        }
        if(read_size == 0)
        {
            puts("Client disconnected");
            fflush(stdout);
        }
        else if(read_size == -1)
        {
            perror("recv failed");
        }
	}
	
	if (new_socket<0)
	{
		perror("accept failed");
		return 1;
	} 

        return 0;
}