// myext.c - myext module
#include <stdio.h>
#include <stdlib.h>
#include <python2.7/Python.h>
#include "myfuncs.h"

// int greeting(char *);
static char py_greeting_doc[] =
    "greeting(s): greetings to you\n";

static PyObject *py_greeting(PyObject *self) {
    int nc = greeting("from C");    // call C function
    return Py_BuildValue("i", nc);
}

// double mult(double, double);
static char py_mult_doc[] = "mult(x, y): mult two doubles\n";

static PyObject *py_mult(PyObject *self, PyObject *args) {
    double arg1, arg2, result; 
    if (!PyArg_ParseTuple(args, "dd", &arg1, &arg2))
        return NULL;
    result = mult(arg1, arg2);     // call C function
    return Py_BuildValue("d", result);
}

// int replace(char *, char, char);
static char py_replace_doc[] = 
    "replace(s, oc, nc): replace chars\n";

static PyObject * 
py_replace(PyObject *self, PyObject *args, PyObject *kwargs) {
    static char *argnames[] = { "string", "old", "new", NULL };
    char *s, *news; char oldc, newc; int nrep; PyObject *result;
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, 
        "scc", argnames, &s, &oldc, &newc))
        return NULL;
    news = (char *)malloc(strlen(s)+1);
    strcpy(news, s);
    nrep = replace(news, oldc, newc);    // call C function
    result = Py_BuildValue("(si)", news, nrep);
    free(news);
    return result; 
}

// double slope(Point *, Point *);
static char py_slope_doc[] = "slope(p1, p2): slope of two Points\n";

static PyObject *py_slope(PyObject *self, PyObject *args) {
    Point p1, p2;
    double result;
    if (!PyArg_ParseTuple(args, "(dd)(dd)", 
            &p1.x, &p1.y, &p2.x, &p2.y))
        return NULL;
    result = slope(&p1, &p2);       // call C function
    return Py_BuildValue("d", result);
}

// int divide(int, int, int *);
static char py_divide_doc[] = 
    "divide(x, y): divide two ints, return int remainder\n";

static PyObject *py_divide(PyObject *self, PyObject *args) {
    PyErr_SetString(PyExc_NotImplementedError, 
        "divide() not implemented.");
    return NULL;
}

static PyMethodDef myfuncs[] = {
    { "greeting", (PyCFunction)py_greeting, 
        METH_NOARGS, py_greeting_doc },
    { "mult", (PyCFunction)py_mult, 
        METH_VARARGS, py_mult_doc },
    { "replace", (PyCFunction)py_replace, 
        METH_VARARGS | METH_KEYWORDS, py_replace_doc },
    { "slope", (PyCFunction)py_slope, 
        METH_VARARGS, py_slope_doc },
    { "divide", (PyCFunction)py_divide, 
        METH_VARARGS, py_divide_doc },
    { NULL }
};

PyMODINIT_FUNC initmyext(void) {
    Py_InitModule3("myext", myfuncs, "Extension module myfuncs");
}
