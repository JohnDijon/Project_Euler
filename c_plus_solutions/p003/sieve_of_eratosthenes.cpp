#include <cmath>
#include <vector>

std::vector<int> sieve_of_eratosthenes_vector(int n)
{
	bool* all_num = new bool[n];
	for (int i = 0; i < n; ++i)
	{
		all_num[i] = 1;
	}
	int largest = 0;
	for (int i = 2; i < sqrt(n); ++i)
	{
		for (int j = pow(i, 2); j < n; j = j + i)
		{
			all_num[j] = 0;
		}
	}

	std::vector<int> primes;
	for (int i = 0; i < n; ++i)
	{
		if (all_num[i] == 1)
			primes.push_back(i);
	}

	delete[] all_num;
	all_num = NULL;
	return primes;
}

bool is_prime(int n)
{	
	n = static_cast<double>(n);
	double sqrt_n = sqrt(n)+1;
	for (int i = 2; i < sqrt_n; ++i)
	{
		if (n %  i == 0)
			return false;
	}
	return true;
}


