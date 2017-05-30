// mypython2.c - call Python program from C with args
#include <stdio.h>
#include <python2.7/Python.h>

int main(int argc, char *argv[]) {
    if (argc == 1) {
        argc = 2;
        argv[1] = "123456789";
    }
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    PySys_SetArgv(argc, argv);
    PyRun_SimpleString("execfile('commas.py')");
    Py_Finalize();
    return 0;
}

/****************************************
     $ mypython2
     123,456,789

     $ mypython2 76354398
     76,354,398

*/
