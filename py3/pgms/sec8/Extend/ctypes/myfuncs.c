// myfuncs.c - call these from Python
#include <stdio.h>
#include <string.h>

int greeting(char *name) {
    printf("hello there, %s\n", name);
    return 0;
}

int add(int x, int y) {
    return x + y;
}

double mult(double x, double y) {
    return x * y;
}

int divide(int x, int y, int *rem) {
    *rem = x % y;
    return x / y;
}

double avg(double *buf, int len) {
    int i; double sum = 0.0;
    for (i = 0; i < len; i++)
        sum += buf[i];
    return sum / len;
}

void myfunc(double *pd) {
    *pd = 3.45;
}

int replace(char *s, char old, char new) {
    int num = 0;
    for (; (s = strchr(s, old)); num++)
        *s++ = new;
    return num;
}

typedef struct Point {
    double x;
    double y;
} Point;

double slope(Point *p1, Point *p2) {
    return (p2->y - p1->y) / (p2->x - p1->x);
}
