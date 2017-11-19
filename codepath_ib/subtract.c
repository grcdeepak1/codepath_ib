//
//  subtract.c
//  codepath_ib
//
//  Created by Deepak on 11/19/17.
//  Copyright © 2017 Deepak. All rights reserved.
//
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 *
 * typedef struct ListNode listnode;
 *
 * listnode* listnode_new(int val) {
 *     listnode* node = (listnode *) malloc(sizeof(listnode));
 *     node->val = val;
 *     node->next = NULL;
 *     return node;
 * }
 */
/**
 * @input A : Head pointer of linked list
 *
 * @Output head pointer of list.
 */
#include <stdio.h>
#include <stdlib.h>
#include "main.h"

void FrontBackSplit(listnode* source, listnode** frontRef, listnode** backRef) {
    
    listnode* fast;
    listnode* slow;
    
    if (source==NULL || source->next==NULL) { // length < 2 cases
        *frontRef = source;
        *backRef = NULL;
    }
    else {
        slow = source;
        fast = source->next;
        
        while (fast != NULL) {
            fast = fast->next;
            if (fast != NULL) {
                slow = slow->next;
                fast = fast->next;
            }
        }
        *frontRef = source;
        *backRef = slow->next;
        slow->next = NULL;
    }
}

void reverse(listnode** headRef) {
    listnode* result = NULL;
    listnode* current = *headRef;
    listnode* next;
    while (current != NULL) {
        next = current->next;   // tricky: note the next node
        current->next = result; // move the node onto the result
        result = current;
        current = next;
    }
    *headRef = result;
}

void subtractList(listnode *A, listnode *B) {
    listnode *currA = A;
    listnode *currB = B;
    while(currA != NULL && currB != NULL) {
        currA->val = currB->val - currA->val;
        currA = currA->next;
        currB = currB->next;
    }
}

listnode *merge(listnode *A, listnode *B) {
    listnode *currA = A;
    if (A == NULL)
        return B;
    else if (B == NULL)
        return A;
    
    while (currA->next != NULL) {
        currA = currA->next;
    }
    currA->next = B;
    return A;
}

listnode* subtract(listnode* A)
{
    listnode *frontRef, *backRef;
    FrontBackSplit(A, &frontRef, &backRef);
    reverse(&backRef);
    subtractList(frontRef, backRef);
    reverse(&backRef);
    merge(frontRef, backRef);
    return frontRef;
}

listnode* listnode_new(int val) {
    listnode* node = (listnode *) malloc(sizeof(listnode));
    node->val = val;
    node->next = NULL;
    return node;
}
void Push(struct listnode** headRef, int data) {
    listnode *newnode = NULL;
    newnode = listnode_new(data);
    newnode->next = *headRef; // The '*' to dereferences back to the real head
    *headRef = newnode;
}

listnode* create_list()
{
    listnode *head = NULL;
    int arr[] = {1, 2, 3, 4, 5};
    for(int i=4;i>=0;i--) {
        Push(&head, arr[i]);
    }
    return head;
}

void print_list(listnode *head)
{
    listnode *node = head;
    while(node != NULL)
    {
        node->next ? printf("%d->", node->val) : printf("%d", node->val);
        node = node->next;
    }
    printf("\n");
}