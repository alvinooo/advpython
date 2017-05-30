// myhello.c - myhello module extension
#include <stdio.h>
#include <stdlib.h>
#include <python2.7/Python.h>
#include "myfuncs.h"

// void greeting(char *);
static char py_greeting_doc[] =
    "greeting(): a greeting from C\n";

static PyObject *py_greeting(PyObject *self) {
    greeting("from C");     // call C function
    Py_RETURN_NONE;         // void return type
}

static PyMethodDef myfuncs[] = {
    { "greeting", (PyCFunction)py_greeting, 
        METH_NOARGS, py_greeting_doc },
    { NULL }
};

PyMODINIT_FUNC initmyhello(void) {
    Py_InitModule3("myhello", myfuncs, "Extension module myhello");
    printf("C: initializing myhello module\n");
}
