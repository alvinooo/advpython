// sortarray.c - sort array elements in place

void sortArray(int size, int *array) {
    register int i, j, temp;
    for (i = 0; i < size; i++)
        for (j = i+1; j < size; j++)
            if (array[i] > array[j]) {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
}
