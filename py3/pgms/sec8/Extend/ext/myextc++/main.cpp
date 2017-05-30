// main.cpp - call these object methods from C++
#include <iostream>
using namespace std;
#include "MyClass.h"

int main() {
    MyClass m(12);
    cout << m.getNum() << endl;
    return 0;
}

/****************************************
     $ main
     12

*/
