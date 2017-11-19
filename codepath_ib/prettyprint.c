/**
 * @input A : Integer
 *
 * @Output 2D int array. You need to malloc memory for result 2D array.
 * Fill in number_of_rows as row, number_of_columns as columns
 * N=4
 * Output=
 * 4 4 4 4 4 4 4
 * 4 3 3 3 3 3 4
 * 4 3 2 2 2 3 4
 * 4 3 2 1 2 3 4
 * 4 3 2 2 2 3 4
 * 4 3 3 3 3 3 4
 * 4 4 4 4 4 4 4
 */
#include <stdlib.h>

int ** prettyPrint(int N, int *number_of_rows, int *number_of_columns) {
    *number_of_rows = 2*N-1;
    *number_of_columns = 2*N-1;
    int i, j, k;
    int sz = 2*N - 1;
    int **a;
    
    // Malloc memory for whole 2D array
    a = (int **) malloc(sizeof(int *) * sz);
    for (k = 0; k < sz; k++) {
        a[k] = (int *) malloc(sizeof(int) * sz);
    }
    
    // Make the first quarter
    for (i = 0; i < N; ++i)
    {
        for (j = 0; j < N; ++j)
        {
            if (j <= i)
                a[i][j] = N - j;
            else
                a[i][j] = N - i;
        }
    }
    
    // Take the mirror image of 2nd quarter
    for (i = 0; i < N; ++i)
    {
        for (j = sz - 1; j >= N; --j)
        {
            a[i][j] = a[i][sz - 1 - j];
        }
    }
    
    // Take water image of below half
    for (i = sz - 1; i >= N; --i)
    {
        for (j = 0; j < sz; ++j)
        {
            a[i][j] = a[sz - 1 - i][j];
        }
    }
    
    return a;
}


