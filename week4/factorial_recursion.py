def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    return n * factorial(n-1)

print(factorial(5))

#tail recursion
def factorialTR(n, ans = 1)
  if n == 1 or n == 0:
    return 1
  elif n < 0:
    return 0
  return factorialTR(n-1, n * ans)