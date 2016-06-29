//Incomplete version for pa2 cs315 Spring 2015  - level m2
//
// File: main.cpp
// Author: developed for CS315 CS-UK JWJ
// Description:  This program finds the minimal
// spanning tree using Kruskal's algorithm.
// Input and output are as specified by the
// instructor.
//Note: for our project the input is an UNDIRECTED graph

#include <cstdlib> // exit
#include <iostream>
#include <fstream>
#include <queue>
#include "graph.h"
#include "edge.h"
#include "unionfind.h"

using namespace std;
int weight=0;

int main(int argc, char *argv[])
{

priority_queue<edge> edges_pq;

  ///////////////////////////////////////////////////
  // open text file for reading
  if(argc != 2)
  {
    // Hint to user about how to use command line
    fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
    exit(1);
  }

  ifstream in;
  in.open(argv[1]);  //open input stream.

  if(!in)         //check for open success.
  {
    cout << "no input file read !!" << endl;
    exit(1);
  }
  ///////////////////////////////////////////////////

	//graph info
	int s;		//graph size
	char t;		//graph type

//Read input and create graph
//TODO: read the number of required cities
//TODO: read the cities and index them to know their indices in the matrix
	in >> s; //size
	t = UNDIRECTED; //needed for our undirected graphs
	graph m(s, t);  //construct see graph.h and graph.cpp

	m.read(in);
  	in.close();

	graph kruskal_tree(s, t);

//Kruskal's algorithm
//TODO: add the required edges

//set PQ
	for(int i=1; i <= s; i++){
		for (int j=i; j <= s; j++){
			if (m.edge(i,j)){
				edge e(i, j, m.edge_weight(i,j));
				edges_pq.push(e);
			}
		}
	}

//Build the subnetwork

	edge edge_temp;
	unionfind un(m.size()+1);
	int kruskal_size=0;
		
	while(!edges_pq.empty()){
		edge_temp=edges_pq.top();

	if(un.find(edge_temp.get_from()) == un.find(edge_temp.get_to()))
		edges_pq.pop();
	else 
		{
		un.unions(un.find(edge_temp.get_from()), un.find(edge_temp.get_to()));
		weight+=edge_temp.get_weight();		
		kruskal_size++;
		}		
	}

//TODO: print the number of edges
	//m.printer(); //print the graph (see graph.h and graph.cpp
	cout << weight << endl;
	return 0;
}
