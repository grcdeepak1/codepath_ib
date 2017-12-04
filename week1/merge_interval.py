# Given a collection of intervals, merge all overlapping intervals.

# For example:

# Given [1,3],[2,6],[8,10],[15,18],

# return [1,6],[8,10],[15,18].

# Make sure the returned intervals are sorted.

def merge(self, intervals):
    stack = []
    intervals = sorted(intervals)
    stack.append(intervals[0])

    for index, interval in enumerate(intervals):
        if (index == 0):
            continue
        if (stack[-1][1] < interval[0]):
            stack.append(interval)
        elif (interval[1] > stack[-1][1]):
            stack[-1][1] = interval[1]

    return stack