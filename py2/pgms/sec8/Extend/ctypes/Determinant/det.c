// det.c - calc determinant of a two-dim array of doubles 

double det(double a[4][4], int n) {
    register int i, j, k;
    double ret;     // determinant
    double x;       // temp
    
    /* determinant algorithm using rows and columns */
    for (k = 0; k < n - 1; k++)
        for (i = k + 1; i < n; i++) {
            x = a[i][k]/a[k][k];
            for (j = k; j < n; j++)
                a[i][j] = a[i][j] - x * a[k][j];
        }
    
    for (ret = 1, i = 0; i < n; i++)
        ret *= a[i][i];
    return ret;
}

typedef struct MyStruct{
    double array[4][4];
} MyStruct;

double getDeterminant(MyStruct *m) {
    return det(m->array, 4);
}
