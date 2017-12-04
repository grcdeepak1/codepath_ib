//
//  main.c
//  string
//
//  Created by Deepak on 11/26/17.
//  Copyright © 2017 Deepak. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * reverseWords(char *str)
{
    int len = (int) strlen(str);
    int i = len-1;
    char *buf = malloc(len*sizeof(char));
    int start = 0, end = 0;
    char c = ' ';
    while (i >= 0) {
        c = str[i];
        if (str[i] == ' ' || i == 0) {
            memcpy(&buf[start], &str[i+1], end);
            memcpy(&buf[start+end], &c, 1);
            start = start + end + 1;
            end = 0;
        } else {
            end++;
        }
        i--;
    }
    buf[len-1] = '\0';
    printf("\n%s\n", buf);
    return  buf;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    char str[40] = "I cool am";
    
    reverseWords(str);
    
    return 0;
}
