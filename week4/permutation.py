class Solution:
  # @param A : list of integers
  # @return a list of list of integers
    def permuteHelper(self, A, chosen, listOfList):
        if (len(A) == 0):
            listOfList.append(chosen[:])
        else:
            for i in range(0, len(A)):
                #Choose
                n = A[i]
                A.remove(n)
                chosen.append(n)

                #Explore
                self.permuteHelper(A, chosen, listOfList)

                #Unchose
                chosen.remove(n)
                A.insert(i, n)

    def permute(self, A):
        chosen = []
        listOfList = []
        self.permuteHelper(A, chosen, listOfList)
        return listOfList