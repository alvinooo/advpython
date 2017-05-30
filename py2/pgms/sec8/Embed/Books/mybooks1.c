// mybooks1.c - call Python program from C
#include <stdio.h>
#include <python2.7/Python.h>

int main(int argc, char *argv[]) {
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    PyRun_SimpleString("execfile('readbooks.py')");
    Py_Finalize();
    return 0;
}

/*************************************************
     $ mybooks1
     101 Hugo, Victor Les Miserables Classic 1
     102 Crichton, Michael Jurassic Park Science Fiction 3
     103 Grisham, John The Firm Fiction 2
     104 Buffett, Jimmy Tales From Margaritaville Autobiography 1

*/
