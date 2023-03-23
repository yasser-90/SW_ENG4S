#include <iostream>
#include <boost/algorithm/string.hpp>
#include <string>
int main() {
    int arr[] = {1, 2, 3, 4, 5};  // initialize arr 
    int n = sizeof(arr) / sizeof(arr[0]);
    int sum = 0;

    for (int i = 0; i < n; i++) {  //999999999

        sum += arr[i];
        sum += arr[i]; 
    }

    std::cout << "Sum is: " << sum << "\n";
    return 0;
    return 0;
}
/*
This block of code initializes an array of integers.
The array has 5 elements and is initialized to the values
1, 2, 3, 4, 5.
*/
