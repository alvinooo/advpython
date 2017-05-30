// mybooks1.c - call python pgm from C
#include <stdio.h>
#include <python2.7/Python.h>

int main(int argc, char *argv[]) {
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    PyRun_SimpleString("execfile('readbooks.py')");
    Py_Finalize();
    return 0;
}

/****************************************
     $ mybooks1
#    (101, u'Hugo, Victor', u'Les Miserables', u'Classic', 1)
#    (102, u'Crichton, Michael', u'Jurassic Park', u'Science Fiction', 3)
#    (103, u'Grisham, John', u'The Firm', u'Fiction', 2)
#    (104, u'Buffett, Jimmy', u'Tales From Margaritaville', u'Autobiography', 1)

*/
