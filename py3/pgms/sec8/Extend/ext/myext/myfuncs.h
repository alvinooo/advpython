// myfuncs.h - call these from Python

int greeting(char *name);
double mult(double x, double y);
int replace(char *s, char old, char new);

typedef struct Point {
    double x;
    double y;
} Point;

double slope(Point *p1, Point *p2);
int divide(int x, int y, int *rem);
