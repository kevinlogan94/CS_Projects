#include <cstdlib> // exit
#include <iostream>
#include <string>
#include <fstream>
#include <queue>
#include <map>
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
	int p;		//pairs
//	int rc;		//required cities
	map<string, int> incities;
	string ctr1;	//the strings your read in 
	map<string, int> ::iterator it;	

//Read input and create graph
//TODO: read the number of required cities
//TODO: read the cities and index them to know their indices in the matrix
	in >> s; //size
	in >> p; //pairs
//	rc = s; //cities needed

	// read in the cities and put them into a map with a designated number.
	for(int i=1; i<=s; i++)
	{
		in >> ctr1;
		incities[ctr1]= i;
	}
//	cout << incities["Lexington"] << incities["Louisville"] << incities["Paducah"] << incities["Corbin"];

	t = UNDIRECTED; //needed for our undirected graphs
	graph m(s, t);  //construct see graph.h and graph.cpp

	int ctr=0;
//	read in the matrix and check if it is connected
	ctr = m.read(in,ctr);
//	print out if it's not connected and is impossible: EC
	if (ctr==s)
	{
		cout << "IMPOSSIBLE" << endl;
		return 1;
	}

	vector<string> first; //the from vector
	vector<string> second; //the two vector
	
	//Check if the pairs are in order from least to greatest, if not fix it.
	string o;
	string u;
	int matnum2;
	int matnum;
	string hold;
	if (p > 0)
	{
	for (int i; i < p; i++)
		{
			in >> o;
			matnum=incities[o];
			//matnum= it->second;
			in >> u;
			matnum2=incities[u];
			//matnum2= it->second;	
			
			if(matnum > matnum2)
			{
				hold = o;
				o=u;
				u = hold;		
			}

			first.push_back(o);
			second.push_back(u);
		} 
	}

/*	for (int i=0; i<p; i++)
	{
		cout << first[i] << " " << second[i] << endl;
	}
*/
  	in.close();

	graph kruskal_tree(s, t);

//Kruskal's algorithm
/*
int kruskal_size = 0;
int row;
int column;
for (int i =0; i<p; i++)
{
	row = incities[first[i]];
	column = incities[second[i]];
	weight += m.edge_weight(row,column);
	kruskal_size++;
}
*/


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
	int kruskal_size = 0;
	int row;
	int column;
	// read in the required edges and check them
	for (int i =0; i<p; i++)
	{
        	row = incities[first[i]];
        	column = incities[second[i]];
		un.unions(un.find(row),un.find(column));
        	weight += m.edge_weight(row,column);
        	kruskal_size++;
	}
		
	while(!edges_pq.empty()){
		edge_temp=edges_pq.top();

	if(un.find(edge_temp.get_from()) == un.find(edge_temp.get_to()))
	{	edges_pq.pop();
	}
	else 
		{
		
		un.unions(un.find(edge_temp.get_from()), un.find(edge_temp.get_to()));
		weight+=edge_temp.get_weight();	
		kruskal_size++;
		}		
	}

//      print the number of edges
//	m.printer(); //print the graph (see graph.h and graph.cpp
	cout << kruskal_size << endl;
	cout << weight << endl;
	return 0;
}

