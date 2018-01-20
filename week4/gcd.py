def gcd(A, B):
    print(A, B)
    if A < B:
        A, B = B, A

    if B == 0:
      return A

    return gcd(B, A % B)

print(gcd(32, 14))