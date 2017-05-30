// myext.c - myext module
#include <stdio.h>
#include <python2.7/Python.h>
#include "myfuncs.h"

// int greeting();
static char py_greeting_doc[] =
    "greeting(s): greetings to you\n";
static PyObject *py_greeting(PyObject *self) {
    int nc = greeting("from C");
    return Py_BuildValue("i", nc);
}

// int add(int, int);
static char py_add_doc[] = "add(x, y): add two ints\n";
static PyObject *py_add(PyObject *self, PyObject *args) {
    int arg1, arg2, res; 
    if (!PyArg_ParseTuple(args, "ii:add", &arg1, &arg2))
        return NULL;
    res = add(arg1, arg2);
    return Py_BuildValue("i", res);
}

// double mult(double, double);
static char py_mult_doc[] = "mult(x, y): mult two doubles\n";
static PyObject *py_mult(PyObject *self, PyObject *args) {
    double arg1, arg2, res; 
    if (!PyArg_ParseTuple(args, "dd:mult", &arg1, &arg2))
        return NULL;
    res = mult(arg1, arg2);
    return Py_BuildValue("d", res);
}

// int divide(int, int, int *);
static char py_divide_doc[] = 
    "divide(x, y): divide two ints, return int remainder\n";
static PyObject *py_divide(PyObject *self, PyObject *args) {
    int arg1, arg2, arg3, res;
    if (!PyArg_ParseTuple(args, "iii:divide", &arg1, &arg2, &arg3))
        return NULL;
    // need PyCapsule here?
    res = divide(arg1, arg2, &arg3);
    return Py_BuildValue("i", res);
}

static PyMethodDef myfuncs[] = {
    { "greeting", (PyCFunction)py_greeting, 
        METH_NOARGS, py_greeting_doc },
    { "add", (PyCFunction)py_add, 
        METH_VARARGS, py_add_doc },
    { "mult", (PyCFunction)py_mult, 
        METH_VARARGS, py_mult_doc },
    { "divide", (PyCFunction)py_divide, 
        METH_VARARGS, py_divide_doc },
    { NULL }
};

void initmyext(void) {
    Py_InitModule3("myext", myfuncs, "Extension module myfuncs");
    printf("C: initializing myext module\n");
}
