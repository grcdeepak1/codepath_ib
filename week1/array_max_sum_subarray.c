/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 * https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
 */
int maxSubArray(const int* arr, int len) {
    int maxSoFar = INT_MIN;
    int maxNow = 0;
    int i=0;
    for(i=0;i<len;i++) {
        maxNow += arr[i];
        if (maxNow > maxSoFar)
            maxSoFar = maxNow;
        if (maxNow < 0)
            maxNow = 0;
    }
    return maxSoFar;
}