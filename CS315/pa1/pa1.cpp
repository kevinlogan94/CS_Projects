#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

//function that tells the binary search to go up
void up(vector<int> ws, int &mid, int &top, int &bot, int &comparison){
		int placement=0;
		for(int t=bot; t<=top; t++)
		{
			if(ws[t]==mid)
			{
				comparison++;
				placement=t;
				bot = t+1;
			}
			
		}
		int place=(top+bot)/2;
		mid=ws[place];
		return;

	}
//function that tells the binary search to go down
void down(vector<int> ws, int &mid, int &top, int &bot, int &comparison)
{
	int top2;
	int placement;
		for(int t=bot; t<=top; t++)
		{
			if(ws[t]==mid)
			{
				comparison++;
				placement=t;
				top2 = t;
			}

		}

		top=top2;
		placement=(top+bot)/2;
		mid=ws[placement];
		return;
}


int main()
{
	//input the amount of elements to be in tsequence
	int amount;
	cout << "Input" <<endl;
	cin >> amount;
	
	vector<int> ts;

	int input;

	//enter the elements to go into tsequence
	for(int i=0; i<amount;i++)
	{
		cin>>input;

		ts.push_back(input);
	}



	vector<int> ws;
// makes the bottom 0
// makes the top the sum of every number in the sequence
// Makes the mid the center between top and bot
	int top=0;
//	int mid=0;
	int bot=0;
	for (int i=0; i<amount; i++)
	{
		
		top=ts[i]+top;
//		mid=ts[i]+mid;
		

	}

	int mid = top/2;

	for (int i = 0; i<=top;i++)
	{
		ws.push_back(i);
	}


	int ctr=0;
	int ctr2=0;
	int ctr3=0;
	int ctr4=0;
	
	int comparison=0;

	int D=0;

while(ctr4==0)
{

	int test = ts[0]-mid;



	for (int i=1; i<amount; i++)
	{
		//Checks if the mid number can work as a valid D
		if(ts[i]-mid>test)
		{
			test=ts[i]-mid;
			ctr2++;
			comparison++;
		}
		else if((ts[i]-mid <= test) && (ts[i]+mid > test))
		{
			test++;
			ctr2++;
			comparison++;
		}
	}
	//tells the binary search if you have to move the sequence up or down
	if (ctr2==amount-1)
	{
	D=mid;
	down(ws, mid, top, bot, comparison);
	comparison++;
	}
	else
	{
	up(ws, mid, top, bot, comparison);
	comparison++;
	}

	if(top==bot)
	{
		ctr4++;
		comparison++;
	}
	ctr2=0;
}
	//prints out the lowest possible D-smooth
	cout << endl << "Output"<< endl << D << endl;
	//print out the comparisons
	cout << "Comparison #" << endl << comparison << endl;
	return 0;
}
