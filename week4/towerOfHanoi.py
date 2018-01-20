def moveSingleDisc(src, dst, ans):
    ans.append(src+dst)

def moveTower(n, src, dst, tmp, ans):
    if n > 0:
        moveTower(n-1, src, tmp, dst, ans)
        moveSingleDisc(src, dst, ans)
        moveTower(n-1, tmp, dst, src, ans)

def move(n):
    ans = []
    moveTower(n, "A", "C", "B", ans)
    return ans

print(move(3))