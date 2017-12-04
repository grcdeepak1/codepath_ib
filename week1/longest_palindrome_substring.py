# Challenge 5 - Longest Palindromic Substring
# Write a program which takes a String as input and returns a String which is the longest palindromic substring in the input, given the following assumptions about the input string:

# its maximum length is 1000
# it contains one unique, longest palindromic substring
# Examples:

# "abdbabbdba" should return "abdba"
# "abdbbbbdba" should return "abdbbbbdba"

def longestPalindrome(A):
  n = len(A)
  dp = [x[:] for x in [[False] * n] * n]

  for i in range(0, n):
      dp[i][i] = True

  for length in range(2, n+1):
      for i in range(0, n-length+1):
          j = i+length-1
          if (length == 2 and (A[i] == A[j])):
              dp[i][j] = True
          elif (A[i] == A[j] and dp[i+1][j-1]):
              dp[i][j] = True

  start     = -1
  max_len   = -1
  for i in range(0, n):
      for j in range(i, n):
          if (dp[i][j] and j-i+1 > max_len):
              max_len = j-i+1
              start = i
return A[start:start+max_len]

text = "abdbabbdba"
text = "abdbbbbdba"
print(longest_palindorme(text))