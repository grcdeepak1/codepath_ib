from collections import namedtuple
from collections import deque

def canReach(x1, y1, x2, y2):
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    queue = deque([p1])

    while len(queue) > 0:
        p = queue.popleft()
        print(p, p2)
        if p == p2:
            return True
        elif p.x > p2.x and p.y > p2.y:
            return False
        else:
            queue.append(Point(p.x+p.y, p.y))
            queue.append(Point(p.x, p.x+p.y))



print(canReach(1, 4, 5, 9))
print(canReach(1, 2, 2, 1))