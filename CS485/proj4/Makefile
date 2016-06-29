# A basic Makefile for the shellex code in the Systems Programming Book
CC = gcc
CFLAGS = -Wall -g
INCLUDES = -I.
LIBS =  -lpthread
SRCS = client.c csapp.c
OBJS = client.o csapp.o
EXE = rrsh-client

all:	$(EXE)

$(EXE):	$(OBJS) 
	$(CC) -o $(EXE) $(CFLAGS) $(INCLUDES) $(OBJS) $(LIBS)

.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@

clean:
	$(RM) *.o *~ $(EXE)

