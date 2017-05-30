// mypython.c - call Python interpreter from C
#include <stdio.h>
#include <python2.7/Python.h>

int main() {
    Py_Initialize();
    printf("Enter Python interpreter...\n");
    PyRun_InteractiveLoop(stdin, "<stdin>");
    printf("Exit Python interpreter...\n");
    Py_Finalize();
    return 0;
}

/****************************************
     $ mypython
     Enter Python interpreter...
     >>> n = 12
     >>> n
     12
     >>> 
     Exit Python interpreter...
     $

*/
