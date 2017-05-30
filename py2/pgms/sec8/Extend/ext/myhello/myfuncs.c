// myfuncs.c - call this from Python
#include <stdio.h>
#include "myfuncs.h"

void greeting(char *name) {
    printf("hello there, %s\n", name);
}
