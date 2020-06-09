//date: 5/20/2020

#include <fstream>
#include <iostream>
#include <string>
#include <map>



int main()
{
	const std::string in_path = "numbers.txt";
	
	std::ifstream in(in_path);
	std::string buffer;
	int total_count = 0;

	int first_ten = 0;
	//1-9
	for (std::string buffer; buffer != "[break]"; std::getline(in, buffer))
	{
		first_ten += buffer.size();
	}
	total_count += first_ten;
	//10-19
	for (std::string buffer; buffer != "[break]"; std::getline(in, buffer))
	{
		total_count += buffer.size();
	}

	//20-99
	for (std::string buffer; std::getline(in, buffer) && buffer != "[break]"; )
	{// for every new ten we count:  n x 10 time + 1 x fist_count (1-9)
		if (buffer == "")
		{
			continue;
		}
		total_count += buffer.size()*10 + first_ten;
	}
	int first_hundred = total_count;
	//100-999
	int hundred = std::string("hundred").size();
	int hundred_and = std::string("hundredand").size();
	total_count += hundred * 9 + first_ten;	//x hundred
	total_count += first_ten * 99 + hundred_and * 99 * 9 + first_hundred * 9; //x hundred and y
	//1000
	total_count += std::string("one").size() + std::string("thousand").size();
	std::cout << total_count;
}


