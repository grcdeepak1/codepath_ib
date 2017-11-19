//
//  main.c
//  codepath_ib
//
//  Created by Deepak on 11/19/17.
//  Copyright © 2017 Deepak. All rights reserved.
//

#include "main.h"
int main(int argc, const char * argv[]) {
    
    // prettyPrint
    int **pArr = NULL;
    int N = 4;
    int numCols = 0, numRows =0;
    pArr = prettyPrint(N, &numRows, &numCols);
    for (int i=0; i< numRows; i++) {
        for (int j=0; j< numCols; j++) {
            printf("%d ", pArr[i][j]);
        }
        printf("\n");
    }
    
    // numRange
    int A[] = {10, 5, 1, 0, 2};
    int numContRange = 0;
    numContRange = numRange(A, 5, 6, 8);
    printf("\nnumContRange : %d\n", numContRange);
    
    // kthSmallest
    int B[] = {2, 1, 4, 3, 2};
    int kth;
    kth = kthsmallest(B, 5, 3);
    printf("\nkthsmallest : %d\n", kth);
    
    return 0;
}