// main.c - call these functions from C
#include <stdio.h>
#include "myfuncs.h"

int main() {
    printf("%d\n", greeting("from C"));

    double val = mult(2.5, 3.5);
    printf("%g\n", val);

    char s[] = "radar";
    int rep = replace(s, 'r', 'm');
    printf("number of changes = %d\n", rep);
    printf("%s\n", s);

    Point p1 = { 5, 10 };
    Point p2 = { 2, 6 };
    double ps = slope(&p1, &p2);
    printf("%g\n", ps);

    int rem;
    int answer = divide(9, 4, &rem);
    printf("answer = %d\n", answer);
    printf("remainder = %d\n", rem);
    return 0;
}

/****************************************
     $ main
     hello there, from C
     20
     8.75
     number of changes = 2
     madam
     1.33333
     answer = 2
     remainder = 1

*/
