// p003.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

bool is_prime(int n)
{
	n = static_cast<double>(n);
	double sqrt_n = sqrt(n) + 1;
	for (int i = 2; i < sqrt_n; ++i)
	{
		if (n % i == 0)
			return false;
	}
	return true;
}

int main()
{	
	long long int n = 100;
	long long double check;
	int q = 1;
	while (check < n)
	{
		check = 6q - 1;
		if (n%check == 0)

	}
}
