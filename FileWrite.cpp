#include <fstream>

int main () 
{
	// Creates a new instance of ofstream.
	std::ofstream myfile;
	
	// Creates/Opens the file.
	myfile.open("exampleText.txt");
	
	// "Prints/Writes" the contents to the file.
	myfile << "Writing to file.\n";
	
	// Always be sure to close your stream…
	myfile.close();
	
	return 0;
}
