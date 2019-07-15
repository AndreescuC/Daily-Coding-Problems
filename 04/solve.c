int seggregateNegatives(int *array, int n)
{
    int i, j=0, aux;
    for (i = 0; i < n; i++) {
        if (array[i] <= 0) {
            aux = array[i];
            array[i] = array[j];
            array[j] = aux;
        }
    }

    array = array + j;
    return n - j;
}

int getMissing(int* array, int size)
{
    int i;
    int new_size = seggregateNegatives(array, size);

    for (i = 0; i < new_size; i++) {
        array[array[i] - 1] = -array[array[i] - 1];
    }

    for (i = 0; i < new_size; i++) {
        if (array[i] > 0) {
            return i + 1;
        }
    }

    return -1;
}
