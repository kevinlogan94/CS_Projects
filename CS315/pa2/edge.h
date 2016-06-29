class edge
{
	public:
	edge();
	edge(int from, int to, int weight);

	int get_from(void) const;
	int get_to(void) const;
	int get_weight(void) const;

	bool operator< (const edge &y) const;

	private:
	int _from, _to, _weight;
};

