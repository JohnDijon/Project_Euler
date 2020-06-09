
#include <iostream>
#include <vector>

// solution using loops (probably faster)
std::vector<int> fib_loop()
{
	int a = 0;
	int b = 1;
	int c = 0;
	std::vector<int> even_fib;
	while (c <= 4000000)
	{
		c = a + b;
		a = b;
		b = c;
		if (c % 2 == 0)
		{
			even_fib.push_back(c);
		}
	}
	return even_fib;
}

// solution using recursion (probably slower, since each number is generated looping through all previous numbers)
int fib_num_recur(int num)
{
	if (num < 2)
		return num;
	else
		return fib_num_recur(num - 1) + fib_num_recur(num - 2);
}
std::vector<int> fib_recur()
{	
	int i = 0;
	int fib_num = 0;
	std::vector<int> even_fib;
	do 
	{
		i += 1;
		fib_num = fib_num_recur(i);
		if (fib_num % 2 == 0)
		{
			even_fib.push_back(fib_num);
		}

	} while (fib_num < 4000000);
	return even_fib;
}


int main()
{
	std::vector<int> even_fib;
	std::vector<int> recur_even_fib;
	even_fib = fib_loop();
	recur_even_fib = fib_recur();
	int sum = 0;
	for (auto n : even_fib)
	{
		sum += n;
	}
	std::cout << sum << std::endl;
	sum = 0;
	for (auto n : recur_even_fib)
	{
		sum += n;
	}
	std::cout << sum;
}
