# Challenge 4 - Palindrome detection
# A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward, e.g., madam or nurses run.

# Write a program which takes a String as input and returns a boolean value which is true if the input is a palindrome and false if it is not, considering only alphanumeric characters and ignoring case.

# Example:

# "A man, a plan, a canal: Panama" is a palindrome and should return true
# "race a car" is not a palindrome and should return false

def is_palindrome(text):
    start_index = 0
    end_index   = len(text) - 1

    while (start_index < end_index):
        if (text[start_index].isalnum() == False):
            start_index += 1
        elif (text[end_index].isalnum() == False):
            end_index -= 1
        elif (text[start_index].upper() == text[end_index].upper()):
            start_index += 1
            end_index -= 1
        else:
            return False
    return True

text = "A man, a plan, a canal: Panama"
text = "race a car"
print(is_palindrome(text))