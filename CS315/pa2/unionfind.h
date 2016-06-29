class unionfind 
{
	public:

	unionfind(int); 
	void unions(int i, int j); 
	int find(int i);

	private:
	int *p; // parent in the tree representing a set
	int size;
};

