//
//  main.h
//  codepath_ib
//
//  Created by Deepak on 11/19/17.
//  Copyright © 2017 Deepak. All rights reserved.
//

#ifndef main_h
#define main_h

#include <stdio.h>

typedef struct listnode {
    int val;
    struct listnode *next;
}listnode;

int ** prettyPrint(int N, int *number_of_rows, int *number_of_columns);
int numRange(int* A, int n1, int B, int C);
int kthsmallest(int* A, int n1, int k);
int* nextGreater(int* A, int n1, int *len1);
listnode* create_list(void);
listnode* subtract(listnode* A);
void print_list(listnode* A);
#endif /* main_h */
