# Challenge 6 - Longest Common Prefix
# Write a program which takes a String[] as input and returns a String which is the longest common prefix, or an empty string if there is none.

# Examples:

# {"bceefgh", "bcfghijk", "bcefgh"} should return "bc"
# {"abcdefgh", "aefghijk", "abcefgh"} should return "a"
# {"", "aefghijk", "abcefgh"} should return ""

def longestCommonPrefix(words):
    num_words = len(words)
    if (num_words == 0):
        return ""

    #find min len of the list of words
    min_len = 99999
    for w in words:
        min_len = min(min_len, len(w))

    prefix = ""
    for i in range(0, min_len):
        c = words[0][i]
        for j in range(1, num_words):
            if (c != words[j][i]):
                return prefix

        prefix += c
    return prefix


words = ["bceefgh", "bcfghijk", "bcefgh"]
print(longestCommonPrefix(words))