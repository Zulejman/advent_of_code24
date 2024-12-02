#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

void bubbleSort(vector<int>& arr){
	int arr_size = arr.size();

	for (int i = 0; i < arr_size - 1; i++){
		for (int j = 0; j < arr_size - i - 1; j++){
			if (arr[j] > arr[j + 1]){
				swap(arr[j], arr[j+1]);
			}
		}
	}
}


int main(){

	ifstream data_file("input.txt");

	vector<int> left_id;
	vector<int> right_id;
	vector<int> distances;
	string line;
	int distance_sum = 0;


	while (getline(data_file, line)){
		istringstream line_string(line);
		int num1, num2;

		if (line_string >> num1 >> num2){
			left_id.push_back(num1);
			right_id.push_back(num2);
		}
	}

	data_file.close();

	bubbleSort(left_id);
	bubbleSort(right_id);

	for (int i = 0; i < left_id.size(); i++){
		distance_sum += (abs(left_id[i] - right_id[i]));
	}	

	cout << distance_sum;

	return 0;
}
