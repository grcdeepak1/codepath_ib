from collections import defaultdict

def totalHelper(student, graph, visited, ans, total):
    visited.add(student)
    ans.append(student)
    for neighbor in graph[student]:
        if neighbor not in visited:
            total += totalHelper(neighbor, graph, visited, ans, total)

    total += 1
    return total

def total(student1, student2, graph):
    visited = set()
    total = 0
    sumTotal = 0
    for student in [student1, student2]:
        ans = []
        if student not in visited:
            sm = totalHelper(student, graph, visited, ans, 0)
            sumTotal += sm
            total += len(ans)
    return total


def getTheGroups(n, queryType, students1, students2):
    g = defaultdict(list)
    ansArr = []
    for i in range(len(queryType)):
        if queryType[i] == 'Friend':
            g[students1[i]].append(students2[i])
            g[students2[i]].append(students1[i])
        elif queryType[i] == 'Total':
            ansArr.append(total(students1[i], students2[i], g))
    print(ansArr)
    return ansArr

getTheGroups(3, ['Friend', 'Total'], [1, 2], [2, 3])