// myClass.h - C++ class
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
        return new MyClass(num);
    }

    int MyClass_getNum(const MyClass * p) {
        return p->getNum();
    }
}
