class Node:
    def __init__(self, id):
        self.value = value
        self.adjacent = []
    
    def getNode(id):

        
def hasPathDFSHelper(src, dst, visited):
    if (src.id in visited):
        return False
    visited.add(src.id)
    if (src == dst):
        return True
    
    for child in src.adjacent:
        if (hasPathDFSHelper(child, dst, visited)):
            return True
        
    return False
        
def hasPathDFS(src, dst):
    s = getNode(src)
    d = getNode(dst)
    visited = set()
    return hasPathDFSHelper(s, d, visited)


def hasPathBFSHelper(src, dst):
    nextToVisit = []
    visited = set()
    
    nextToVisit.append(src)
    while len(nextToVisit) > 0:
        node = nextToVisit[0]
        del nextToVisit[0]
        
        if (node == dst):
            return True
        
        if (node.id in visited):
            continue
            
        visited.add(node.id)
        
        for child in node.adjacent:
            nextToVisit.append(child)
    
        return False
    
def hasPathBFS(src, dst):
    return hasPathBFSHelper(src.id, dst.id)       
