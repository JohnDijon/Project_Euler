#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

std::string IntToStr(int num)
{
	std::string str_num = "";
	while(num != 0)
	{
		char ch = '0' + num % 10;
		//str_num += num % 10;
		str_num += ch;
		num /= 10;
	}
	//need to reverce string
	int str_size = str_num.size();
	for (int i = 0; i < str_size / 2; i++)
	{
		char temp = str_num[i];
		str_num[i] = str_num[str_size - i - 1];
		str_num[str_size - i - 1] = temp;
 	}
	return str_num;
}

bool IsPalindrome(const std::string& str)
{
	int str_size = str.size();
	for (int i = 0; i < str_size / 2; i++)
	{
		if (str[i] == str[str_size - i - 1])
			continue;
		else
			return false;
	}
	return true;
}


int main()
{
	constexpr int max_num = 999;
	constexpr int limit = 100;
	std::vector<int> palindromes;
	for (int i = max_num; i > max_num - limit; i--)
	{
		for (int j = max_num; j > max_num - limit; j--)
		{
			if (IsPalindrome(IntToStr(i * j)))
			{
				palindromes.push_back(i * j);
			}
		}
	}
	std::sort(palindromes.begin(), palindromes.end(), std::greater<int>());
	std::cout << palindromes[0];
}