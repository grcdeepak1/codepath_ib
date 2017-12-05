def reverseList(A, k):
    stack = []
    cur = A
    prev = None

    while (cur):
        count = 0
        while (cur and count < k):
            stack.append(cur)
            cur = cur.next
            count += 1

        while (len(stack) > 0):
            if (prev == None):
                prev = stack[-1]
                head = prev
                stack.pop()
            else:
                prev.next = stack[-1]
                prev = prev.next
                stack.pop()

    prev.next = None;

    return head