// pgm.cpp - C++ class
#include <iostream>
using namespace std;

class MyClass {
private:
    int num;
public:
    MyClass(int n) {
        num = n;
    }
    int getNum() const {
        return num;
    }
};

extern "C" {
    MyClass *MyClass_new(int num) {
        cout << "C++: new MyClass" << endl;
        return new MyClass(num);
    }

    void MyClass_del(MyClass *p) {
        cout << "C++: delete MyClass obj" << endl;
        delete p;
    }

    int MyClass_getNum(const MyClass & p) {
        cout << "C++: MyClass.getNum()" << endl;
        return p.getNum();
    }
}

