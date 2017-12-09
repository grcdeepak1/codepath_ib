# Challenge 6 - Longest non-repeating substring
# # Write a program which takes as its input a String and returns the length of the longest substring that does not contain any repeated characters.

# # Example: Given the string "abcabcbb", the longest substring with no repeated characters is "abc", so the program would return a value of 3. Given the string "aaaaaaaa", the longest non-repeating substring is "a" and thus the output would be 1.
# 01234567
# abcabcbb
#        ^
#     count:    7-6 = 1
#     MaxCount: 3
#     MaxCountStartIndex = 0
# hash = { a:4, b:6, c:5 }
# Approach:
#     0. initilize a maxCount
#     1. iterate and check if char is in hashmap if not, add in hashmap along with index of char and incr count by 1
#     2. if in hashmap reset the count to curIndex-indexOfCharFound+1
#     3. Re-eval the maxCount and continue to iterate.

def longest_non_repeating_substring(string):
    count = 0
    maxCount = 0
    startIndex = 0
    startIndexOfMaxSubstring = 0
    charHash = {}

    for (i, c) in enumerate(string):
        #If char not in hash
        if charHash.get(c) == None:
            charHash[c] = i
            count += 1
        #If char in hash but outside current substring
        elif (charHash[c] < startIndex):
            charHash[c] = i
            count += 1
        #If char in hash and within current substring
        else:
            startIndex = charHash[c]+1
            count = i - charHash[c]
            charHash[c] = i


        if (count > maxCount):
            maxCount = count
            startIndexOfMaxSubstring = i-maxCount+1

    return maxCount, string[startIndexOfMaxSubstring:startIndexOfMaxSubstring+maxCount]

print(longest_non_repeating_substring("geeksforgeeks"))
#(7, 'eksforg')