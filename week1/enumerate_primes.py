# Challenge 2 - Enumerate all primes <= n
# A prime number (or a prime) is an integer greater than 1 that has no positive divisors other than 1 and itself.

# Write a program which takes as input an int value n and returns an array of int containing all unique primes <= n.

# Example: if the value of n is 8, the function should return: {2,3,5,7}

# Hint: One well-known algorithm for doing this is over 2,000 years old, but it's not the most efficient.

# Remember, you are not allowed to use any primality testing functions.

# Approach:
# Mark every thing as prime
# iterate from 2 to check if it is prime,
# if yes then print that number and continue to iterate and mark all
# multiples of that number as non-prime

# refer: https://www.youtube.com/watch?v=eKp56OLhoQs

import math

def enumerate_prime(n):
    primes = [1]*(n+1)
    primes[0] = 0
    primes[1] = 0
    prime_numbers = []
    for i in range(2, int(math.sqrt(n+1))):
        if (primes[i]):
            j = 2
            while (i*j < n+1):
                primes[i*j] = 0
                j += 1

    for index, i in enumerate(primes):
        if (primes[index] == 1):
            prime_numbers.append(index)

    return prime_numbers

print(enumerate_prime(8))