//
//  next_greater.c
//  codepath_ib
//
//  Created by Deepak on 11/19/17.
//  Copyright © 2017 Deepak. All rights reserved.
//
/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer array. You need to malloc memory, and fill the length in len1
 */
#include <stdio.h>
#include <stdlib.h>

int* nextGreater(int* A, int n1, int *len1) {
    int i, j;
    int *B = (int *) malloc(n1 * sizeof(int *));
    
    for (i = 0; i < n1; i++) {
        if (i == n1-1) {
            // if i is the last element
            B[i] = -1;
            break;
        }
        for (j = i+1; j < n1; j++) {
            if (A[i] < A[j]) {
                // success
                B[i] = A[j];
                break;
            } else if (j == n1-1) {
                // if j is the last element
                B[i] = -1;
            }
        }
    }
    *len1 = n1;
    return B;
}