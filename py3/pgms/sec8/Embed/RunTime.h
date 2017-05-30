// RunTime.h - check C API calls for errors
#include <stdarg.h>

#define check(PTR) _check(PTR, __FILE__, __LINE__)

void _check(void *ptr, const char *file, int lineno) {
    if (PyErr_Occurred()) 
        PyErr_Print();
    if (ptr == NULL) {
        fprintf(stderr, "Error in %s at line %d\n", file, lineno);
        exit(1);
    }
}

void dec_ref_counts(int argc, ...) {
    va_list args;
    va_start(args, argc);
    for (int i = 0; i < argc; i++) {
        void *ptr = va_arg(args, void *);
        //printf("decr reference count for %p\n", ptr);
        Py_DECREF(ptr);
    }
}

