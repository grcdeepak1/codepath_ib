class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findPivot(self, arr, low, high):
        if high < low:
            return -1
        if high == low:
            return low
        mid = low + (high-low)/2
        if (mid < high and arr[mid] > arr[mid+1]):
            return mid
        elif (arr[low] >= arr[mid]):
            return self.findPivot(arr, low, mid-1)
        else:
            return self.findPivot(arr, mid+1, high)


    def binarySearch(self, arr, low, high, key):
        if high < low:
            return -1
        mid = low + (high-low)/2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            return self.binarySearch(arr, mid+1, high, key)
        else:
            return self.binarySearch(arr, low, mid-1, key)

    def search(self, arr, num):
        n = len(arr)
        pivot = self.findPivot(arr, 0, n-1)
        if pivot == -1:
            return self.binarySearch(arr, 0, n-1, num)

        if (arr[pivot] == num):
            return pivot

        if (arr[0] <= num):
            return self.binarySearch(arr, 0, pivot-1, num)
        else:
            return self.binarySearch(arr, pivot+1, n-1, num)



