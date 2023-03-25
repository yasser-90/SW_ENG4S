#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
using namespace std;


int main()
{
    char a;
    int state = 1;

    cout << "enter your text \n" << endl;
    cin >> a;
        while (state <5 )
    {
        switch (state) {

                case 1:
               if (a == '/'){ cin>>a;


                    state = 2;

                }
                else {
                    cout << "something missed in comment / " << endl;
                    state=100;
                }
                break;
            case 2:
              if (a == '*')
              {
                  cin>>a;

                    state = 3;
              }
                else {
                    cout << "something missed in comment * " << endl;
                    state=100;
}

                break;
        /*    case 3:
                  if (a== '*'){
                          cin>>a;
                    state = 4;}
                   else {
                      cin>>a;
                    state = 3;}


                break;
            case 4:

                if (a == '/')
                {
                    state = 5;
                }
                else if (a == '*')
                { */ 

                 cin>>a;
                    state = 4;
                }
                else{
                    cin>>a;
                    state = 3;}
                break;

        }
    }

            if (state == 5)

            cout << " accept";

    //state5:if (state == 5 && statement[counter] != '/') {
            else cout << " reject";


}
