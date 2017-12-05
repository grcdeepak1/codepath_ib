def deleteDuplicates(self, head):
    node = head
    while node:
        nextNode = node.next
        if (nextNode and nextNode.val == node.val):
            node.next = nextNode.next
        else:
            node = node.next
    return head