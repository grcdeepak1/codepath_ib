m = [[1, 0, 1, 1, 0],
     [0, 1, 0, 0, 1],
     [1, 0, 1, 1, 0],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 0, 1]]
t = [1, 2, 3, 4, 5]

def dfs(i, j, m, visited, ans):
    if i < 0 or i > len(m) or j < 0 or j > len(m):
        return

    visited.add((i, j))

    if m[i][j] == 1:
        ans.append((i, j))
    else:
        return

    for (p,q) in [(1,0), (-1, 0), (0, 1), (0, -1)]:
        if i < 0 or i > len(m) or j < 0 or j > len(m):
            continue
        if i+p >= len(m) or j+q >= len(m):
            continue
        if m[i+p][j+q] == 1 and (i+p,j+q) not in visited:
            dfs(i+p, j+q, m, visited, ans)

def countGroups(m, t):
    groups = defaultdict(int)
    visited = set()
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 1 and (i,j) not in visited:
                ans = []
                dfs(i,j, m, visited, ans)
                print(i, j, len(ans))
                groups[len(ans)] += 1
    print(groups)
    for i, n in enumerate(t):
        print(i, n)
        t[i] = groups[n]
    return t



countGroups(m, t)
ans = []
visited = set()
dfs(0, 2, m, visited, ans)
print(ans)