# Challenge 2 - Add two numbers
# In this exercise, we'll use your LinkedListNode implementation to represent a non-negative integer such that each node in the list represents a single digit (in base 10) and the digits are stored in reverse order.

# 1     == 1
# 1→2   == 21
# 1→2→3 == 321
# Write a program which takes as its input two such lists, a and b, and adds them arithmetically one decimal at a time. Your algorithm should traverse both lists together, adding the values for each node and carrying the 1 to the next place when the sum >= 10. The result should be returned as a linked list in the same format as the input lists.

# Examples:

# 1→2     +   5→3   == 6→5      // 21 + 35 == 56
# 1→2     +   1→2→3 == 2→4→3    // 21 + 321 == 342
# 1→2→3   +   7→8→9 == 8→0→3→1  // 321 + 987 == 1308
class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

head1 = Node(1, Node(2, Node(3, None)))
head2 = Node(7, Node(8, Node(9, None)))

def summation(head1, head2):
    node1 = head1
    node2 = head2
    carry = 0
    prev = None
    newHead = None
    while node1 or node2 or carry:
        sumVal = carry

        if node1:
            sumVal += node1.value
            node1 = node1.next

        if node2:
            sumVal += node2.value
            node2 = node2.next
        newNode = Node(sumVal%10, None)

        if prev:
            prev.next = newNode
        else:
            newHead = newNode

        prev = newNode
        carry = sumVal/10
    return newHead

def traverse(head):
    while(head):
        print(head.value)
        head = head.next

head = summation(head1, head2)
traverse(head)