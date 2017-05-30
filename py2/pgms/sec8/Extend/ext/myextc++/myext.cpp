// myext.cpp - myext module in C++
#include <iostream>
#include <python2.7/Python.h>
#include "MyClass.h"

extern "C" {
    // destructor MyClass
    static void del_MyClass(PyObject *obj) {
        cout << "C++: MyClass destr called" << endl;
        delete (MyClass *)PyCapsule_GetPointer(obj, "MyClass");
    }

    static char py_MyClass_new_doc[] = "new MyClass object";

    static PyObject *py_MyClass_new(PyObject *self, PyObject *args) {
        int arg; 
        cout << "C++: MyClass constr called" << endl;
        if (!PyArg_ParseTuple(args, "i", &arg))
            return NULL;
        MyClass *pm = new MyClass(arg);
        return PyCapsule_New(pm, "MyClass", del_MyClass);
    }

    static char py_MyClass_getNum_doc[] = "MyClass getNum()\n";

    static PyObject *py_MyClass_getNum(PyObject *self, PyObject *args) {
        MyClass *arg; 
        PyObject *py;
        cout << "C++: MyClass::getNum() called" << endl;
        if (!PyArg_ParseTuple(args, "O", &py))
            return NULL;
        if (!(arg = (MyClass *)PyCapsule_GetPointer(py, "MyClass")))
            return NULL;
        int num = MyClass_getNum(arg);
        return Py_BuildValue("i", num);
    }

    static PyMethodDef myfuncs[] = {
        { "MyClass_new", (PyCFunction)py_MyClass_new, 
            METH_VARARGS, py_MyClass_new_doc },
        { "MyClass_getNum", (PyCFunction)py_MyClass_getNum, 
            METH_VARARGS, py_MyClass_getNum_doc },
            { NULL }
    };

    PyMODINIT_FUNC initmyext(void) {
        Py_InitModule3("myext", myfuncs, "Extension module myfuncs");
        cout << "C++: initializing myext module" << endl;
    }
}
