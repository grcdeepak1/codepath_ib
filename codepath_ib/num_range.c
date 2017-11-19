//
//  num_range.c
//  codepath_ib
//
//  Created by Deepak on 11/19/17.
//  Copyright © 2017 Deepak. All rights reserved.
//

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * @input B : Integer
 * @input C : Integer
 *
 * @Output Integer
 */
int numRange(int* A, int n1, int B, int C) {
    int sum , cnt = 0;
    for(int i = 0; i<n1; i++)
    {
        sum = A[i];
        if(sum >= B && sum <= C)
            cnt++;
        for(int j = i+1; j<n1; j++)
        {
            sum += A[j];
            if(sum >= B && sum <= C)
                cnt++;
            if(sum > C)
                break;
        }
    }
    return cnt;
}