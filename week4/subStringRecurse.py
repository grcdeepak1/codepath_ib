def addSubstrings2(index, s, sb, result):
    print('\t'*index + "addSubstrings2 :", index, s)
    if index < len(s):
        sb = sb+s[index]
        result.append(sb)
        addSubstrings2(index+1, s, sb, result)

def addSubstrings(index, s, result):
    print('\t'*index + "addSubstrings :", index, s)
    if index < len(s):
        addSubstrings2(index, s, "", result)
        addSubstrings(index+1, s, result)

def subSubStrings(s):
    result = []
    addSubstrings(0, s, result)
    return result

print(subSubStrings("abc"))