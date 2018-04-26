#include <fstream>
#include <iostream>
#include <string>

int main () 
{
	std::string line;
	
	std::ifstream inputFile("exampleText.txt");
	
	if (inputFile.is_open())
	{
		while (std::getline(inputFile,line))
		{
			std::cout << line << std::endl;
		}
    
		inputFile.close();
	}
	else
	{
		std::cout << "Unable to open file" << std::endl;
	} 
	
	return 0;
}
