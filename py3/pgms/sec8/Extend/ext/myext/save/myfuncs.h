// myfuncs.h - call these from Python

int greeting(char *name);
int add(int x, int y);
double mult(double x, double y);
int divide(int x, int y, int *rem);
double avg(double *buf, int len);
int replace(char *s, char old, char new);

typedef struct Point {
    double x;
    double y;
} Point;

double slope(Point *p1, Point *p2);
