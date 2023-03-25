#include <iostream>
#include <string>
#include <algorithm>
 
/*int main() {
    std::string s = "\rWhitespace String ";

    std::cout << "String s before removing whitespaces: " << s <<
        std::endl << std::endl;

    // Removing whitespaces from string s.
    s.erase(std::remove_if(s.begin(), s.end(),
            [](char c) { // a lambda function
                return (c == ' ' || c == '\n' || c == '\r' ||
                    c == '\t' || c == '\v' || c == '\f');
            }),
        s.end());

    std::cout << "String s after removing whitespaces: " << s;

    return 0;
}*/