// mypython.c - call python time.asctime()
#include <stdio.h>
#include <assert.h>
#include <python2.7/Python.h>
#include "RunTime.h"

int main() {
    Py_Initialize();

    // import mymodule
    // your code here...
 
    // get time.asctime function 
    // your code here...

    // no arg for asctime()
    // your code here...

    // invoke time.asctime()
    // your code here...

    // get string return value
    char buffer[80];
    // your code here...

    // decrement ref counts of PyObject * vars
    // your code here...
 
    Py_Finalize();
    return 0;
}

/****************************************
     $ mypython
     Sat Feb 18 18:48:28 2017

*/
