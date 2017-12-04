# Challenge 3 - Spiral Order
# A matrix is a two-dimensional array of r rows, each with c columns, such that the total number of elements in the matrix is r * c.

# The spiral order of such a matrix is the list of all its elements starting at index (0, 0) and proceeding in clockwise order from the outermost values to innermost values.

# Write a program that takes an int[][] matrix as its input and returns an int[] of all the input's values in spiral order.

# Example: Given the following matrix:

# int[][] matrix = {
#   { 1, 2, 3 },
#   { 4, 5, 6 },
#   { 7, 8, 9 }
# };
# Your program should return {1,2,3,6,9,8,7,4,5}
def spiralOrder(self, A):
    nRow = len(A)
    nCol = len(A[0])
    rMin = 0
    rMax = nRow-1
    cMin = 0
    cMax = nCol-1
    return_arr = []

    while (rMin >= 0 and rMax <= nRow and cMin >= 0 and cMax <= nCol):
        if (rMin > 0):
            cMin += 1
        if (len(range(cMin, cMax+1)) == 0):
            break
        for c in range(cMin, cMax+1):
            return_arr.append(A[rMin][c])

        rMin += 1
        if (len(range(rMin, rMax+1)) == 0):
            break
        for r in range(rMin, rMax+1):
            return_arr.append(A[r][cMax])

        cMax -= 1
        if (len(range(cMax, cMin-1, -1)) == 0):
            break
        for c in range(cMax, cMin-1, -1):
            return_arr.append(A[rMax][c])

        rMax -= 1
        if (len(range(rMax, rMin-1, -1)) == 0):
            break
        for r in range(rMax, rMin-1, -1):
            return_arr.append(A[r][cMin])

  return return_arr