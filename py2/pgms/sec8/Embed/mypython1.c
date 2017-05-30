// mypython1.c - run Python command from C
#include <stdio.h>
#include <python2.7/Python.h>

int main() {
    Py_Initialize();
    PyRun_SimpleString("print 'Hello from Python'");
    Py_Finalize();
    return 0;
}

/****************************************
     $ mypython1
     Hello from Python

*/
