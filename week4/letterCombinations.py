class Solution:
  # @param A : string
  # @return a list of strings
    def letterCombinations(self, A):
        LETTER = {0:'0', 1:'1', 2:['a', 'b', 'c'], 3:['d', 'e', 'f'],
          4:['g', 'h', 'i'],  5:['j', 'k', 'l'],  6:['m', 'n', 'o'],
          7:['p', 'q', 'r', 's'],  8:['t', 'u', 'v'],  9:['w', 'x', 'y', 'z']}
        ans = []
        length = len(A)

        def letterHelper(soFar, index):
            if len(soFar) == length:
                ans.append(soFar)
            else:
                for i in range(len(LETTER[int(A[index])])):
                    letterHelper(soFar+LETTER[int(A[index])][i], index+1)

        letterHelper('', 0)
        return ans