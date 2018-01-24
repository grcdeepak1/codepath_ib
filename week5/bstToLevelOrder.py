# /*
# # Given binary tree
# #     3
# #    / \
# #   9  20
# #     /  \
# #    15   7
#
# # [[3], [9, 20], [15, 7]]
#
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

def printLevelOrder(root, level = 0):
  if root == None:
    return

  nodesToVisit = [(root, level)]
  ans = {}
  while len(nodesToVisit) > 0:
    tup = nodesToVisit[0]
    node, level = tup
    del nodesToVisit[0]

    if level in ans:
      ans[level].append(node.val)
    else:
      ans[level] = [node.val]

    if (node.left):
      nodesToVisit.append((node.left, level+1))
    if (node.right):
      nodesToVisit.append((node.right, level+1))

  return ans.values()


def printInorder(root):
  if root == None:
    return

  print(root.val)
  printInorder(root.left)
  printInorder(root.right)


print(printLevelOrder(root))
