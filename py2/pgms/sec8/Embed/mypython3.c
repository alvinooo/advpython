// mypython3.c - call Python function from C
#include <stdio.h>
#include <assert.h>
#include <python2.7/Python.h>
#include "RunTime.h"

int main(int argc, char *argv[]) {
    if (argc == 1) {
        argc = 2;
        argv[1] = "123456789";
    }
    Py_Initialize();

    // import mymodule
    // PySys_SetPath("."); // bad, can't import other modules
    PyObject *sys_path = PySys_GetObject("path");
    PyList_Append(sys_path, PyString_FromString("."));
    PyObject *module = PyImport_ImportModule("mymodule");
    check(module);

    // get mymodule.commas function 
    PyObject *func = PyObject_GetAttrString(module, "commas"); 
    check(func);

    // create string arg for commas()
    PyObject *args = Py_BuildValue("(s)", argv[1]);
    check(args);

    // invoke mymodule.commas(arg)
    PyObject *py = PyObject_Call(func, args, NULL);
    check(py);

    // get string return value
    char commaString[80];
    strcpy(commaString, PyString_AsString(py));
    printf("C: %s\n", commaString);

    // decrement ref counts of PyObject * vars
    dec_ref_counts(5, args, py, func, module, sys_path);

    Py_Finalize();
    return 0;
}

/****************************************
     $ mypython3
     Python: commas('123456789') invoked
     C: 123,456,789

     $ mypython3 12345
     Python: commas('12345') invoked
     C: 12,345

*/
