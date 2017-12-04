/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 * https://www.interviewbit.com/problems/find-duplicate-in-array/
 */

int repeatedNumber(const int* A, int n1) {
    int a=0;
    int i;
    int b=0;
    for(i=1;i<n1;i++)
        b=b^i;
    for(i=0;i<n1;i++)
        a=a^A[i];
    return (a^b);
}
