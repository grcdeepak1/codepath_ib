class Solution:
  # @param A : list of integers
  # @return a list of list of integers
    def subsetHelper(self, A, chosen, listOfList):
        if (len(A) == 0):
            listOfList.append(sorted(chosen[:]))
        else:
            n = A[0]
            A.remove(n)

            chosen.append(n)
            self.subsetHelper(A, chosen, listOfList)

            chosen.remove(n)
            self.subsetHelper(A, chosen, listOfList)

            A.insert(0, n)

    def subsets(self, A):
        chosen = []
        listOfList = []
        self.subsetHelper(A, chosen, listOfList)
        return sorted(listOfList)