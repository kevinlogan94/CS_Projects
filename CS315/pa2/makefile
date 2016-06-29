# Author: CS315 JWJ-CS-UK
# Task: pa2 - cs315s15 handout
# Description: makefile for building program "pa2m2cs315s15"

pa2m2cs315s15: main.o graph.o edge.o unionfind.o
	g++ -o pa2m2cs315s15 main.o graph.o edge.o unionfind.o

main.o:	main.cpp
	g++ -c -Wall main.cpp

graph.o: graph.h graph.cpp
	g++ -c -Wall graph.cpp

edge.o:	edge.h edge.cpp
	g++ -c -Wall edge.cpp

unionfind.o: unionfind.h unionfind.cpp
	g++ -c -Wall unionfind.cpp


clean:
	rm pa2m2cs315s15
	rm *.o

