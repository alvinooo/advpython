// mypython.c - call python time.asctime()
#include <stdio.h>
#include <assert.h>
#include <python2.7/Python.h>
#include "RunTime.h"

int main() {
    Py_Initialize();

    // import mymodule
    PyObject *module = PyImport_ImportModule("time");
    check(module);
 
    // get time.asctime function 
    PyObject *func = PyObject_GetAttrString(module, "asctime"); 
    check(func);

    // no arg for asctime()
    PyObject *args = Py_BuildValue("()");
    check(args);

    // invoke time.asctime()
    PyObject *py = PyObject_Call(func, args, NULL);
    check(py);

    // get string return value
    char buffer[80];
    strcpy(buffer, PyString_AsString(py));
    printf("%s\n", buffer);

    // decrement ref counts of PyObject * vars
    dec_ref_counts(4, py, args, func, module);
 
    Py_Finalize();
    return 0;
}

/****************************************
     $ mypython
     Sat Feb 18 18:48:28 2017

*/
