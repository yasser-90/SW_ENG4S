#include<iostream>
#include<string>
using namespace std;
void main(){
	string s, s1="world", s2="wor1D";
	char ch;
	int len, size;
	//string s="hello", s1="world"; char ch[5]={ 'a', 'b', 'c', 'd', 'f' };
	//cout << s.append(3, '.') << endl;
	//cout << s.append(s1) << endl;
	//cout << s.assign(3, '.') << endl;
	//cout << s.assign(s1, 2, 3) << endl;
	cout << s.assign(s1) << endl;
	//ch=s.at(3);
	//len=s.length();
	//size=s.size();
    /*cout << ch << len << size << endl;
	cout << s1.compare(0, 2, s2) << endl;
	cout << s.erase(2, 2) << endl;
	cout << s2.erase(0, 1) << endl;
	cout << s.append(s2.at(3));
	cout << s.substr(3, 3) << endl;
	cout << s.replace(0, 3, s2) << endl;*/
	system("pause");}