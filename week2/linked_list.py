# Challenge 1 - Implement a Linked List
# Implement a simple linked list in Java without using any collections classes. The list should be implemented using a single class such that each instance represents a single node in the list, encapsulating the node's value and a reference to the following node, as well as a convenience method to initialize a whole list from an array of values. The class should implement the following interface:

# public interface LinkedListNode<E> {

#     /* getter/setter for this node's value */
#     E getValue();
#     void setValue(E value);

#     /* getter/setter for the subsequent node, or null if this is the last node */
#     LinkedListNode<E> getNext();
#     void setNext(LinkedListNode<E> next);

#     /**
#      * Initialize this node and all of its subsequent nodes from
#      * an array of values, starting with the head value at index 0
#      *
#      * @param listValues - the ordered values for the whole list
#      */
#     void setValuesFromArray(E[] listValues);

# }

class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

  def getValue(self):
    return self.value

  def setValue(self, value):
    self.value = value

  def getNext(self):
    return self.next

  def setNext(self, nextNode):
    self.next = nextNode

  def setValuesFromArray(self, listValues):
    node = self
    prev = node
    for (i, v) in enumerate(listValues):
        if node:
            node.value = v
        else:
            node = Node(v, None)
            prev.next = node
        prev = node
        node = node.next

head = Node(2, Node(2, Node(2, Node(3, Node(3, Node(4, None))))))

def traverseAndInsert(head):
    node = head
    while (node):
        print(node.getValue())
        if (node.next == None):
            node.setValuesFromArray([9,9,9])
            return head
        node = node.next
    return head

def traverse(head):
    node = head
    while (node):
        print(node.value)
        node = node.next

head = traverseAndInsert(head)
print("--")
traverse(head)




