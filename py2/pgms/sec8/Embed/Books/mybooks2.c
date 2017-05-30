// mybooks2.c - call Python module function from C
#include <stdio.h>
#include <assert.h>
#include <python2.7/Python.h>
#include "RunTime.h"

int main(int argc, char *argv[]) {
    if (argc == 1) {
        fprintf(stderr, "Usage: %s [name.db]\n", argv[0]);
        exit(1);
    }
    Py_Initialize();

    // import bookmodule
    PyObject *sys_path = PySys_GetObject("path");
    PyList_Append(sys_path, PyString_FromString("."));
    PyObject *module = PyImport_ImportModule("bookmodule");
    check(module);

    // get bookmodule.totalbooks function 
    PyObject *func = PyObject_GetAttrString(module, "totalbooks"); 
    check(func);

    // create string arg for totalbooks()
    PyObject *args = Py_BuildValue("(s)", argv[1]);
    check(args);

    // invoke bookmodule.totalbooks(arg)
    PyObject *py = PyObject_Call(func, args, NULL);
    check(py);

    // get integer return value
    printf("C: number of books = %ld\n", PyInt_AsLong(py));

    // decrement ref counts of PyObject * vars
    dec_ref_counts(5, args, py, func, module, sys_path);

    Py_Finalize();
    return 0;
}

/****************************************
     $ mybooks2 BookCatalog.db 
     Python: reading BookCatalog.db
     C: number of books = 7

     $ mybooks2 file
     Traceback (most recent call last):
       File "./bookmodule.py", line 14, in totalbooks
         raise TypeError("%s is not a database" %dbase)
     TypeError: file is not a database
     Error in mybooks2.c at line 30

*/
