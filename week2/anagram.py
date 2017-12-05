def anagrams(string):
    anagram_hash = {}
    for index, animal in enumerate(string, 1):
        ascii_sum = 0
        for ch in animal:
            ascii_sum += ord(ch)
        if anagram_hash.get(ascii_sum) != None:
            anagram_hash[ascii_sum].append(index)
        else:
            anagram_hash[ascii_sum] = [index]

    return anagram_hash.values()



print(anagrams(("cat","dog","god","tca")))
#[[1, 4], [2, 3]]