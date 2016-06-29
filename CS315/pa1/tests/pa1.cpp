#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

//function that moves the binary search higher in the sequence
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

//function that moves the binary search lower in the sequence
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
// make bot equal 0
//make your top the sum of all ints in the sequence
//make your mid the middle between top and bot
//	int mid=0;
	int top=0;
	int bot=0;
	for (int i=0; i<amount; i++)
	{
//		mid = ts[i]+mid;

		top=ts[i]+top;

	}

	//take the center the tsequence as your D
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


	//go throught the sequence and check if the mid number could work as a D
	for (int i=1; i<amount; i++)
	{

		if(ts[i]-mid>test)
		{
			comparison++;
			test=ts[i]-mid;
			ctr2++;
		}
		else if((ts[i]-mid <= test) && (ts[i]+mid > test))
		{
			test++;
			ctr2++;
			comparison++;
		}
	}

	//tells the compiler if the binary search should move up or down
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
	//print out the outputted D.
	cout << endl << "Output"<< endl << D << endl;
	cout << "Comparison #" << endl << comparison <<endl;

	return 0;
}
