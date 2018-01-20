def numberOfOnes(n):
    count = 0
    while n:
        if (n & 0x01):
            count += 1
        n = n >> 1
    return count

n = 257
print(numberOfOnes(n))