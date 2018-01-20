def nChooseK(n, k, memo):
    if n == k or k == 0:
        return 1

    if (n,k) in memo:
        return memo[(n,k)]
    else:
        memo[(n,k)] = nChooseK(n-1, k-1, memo) + nChooseK(n-1, k, memo)
        return memo[(n,k)]

memo = {}
print(nChooseK(10, 2, memo))