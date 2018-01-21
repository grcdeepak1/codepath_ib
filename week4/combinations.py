class Solution:
    def combineHelper(self, Array, B, chosen, listOfList):
        if (len(chosen) == B):
            listOfList.append(sorted(chosen[:]))
        elif (len(Array) > 0):
            n = Array[0]
            Array.remove(n)

            chosen.append(n)
            self.combineHelper(Array, B, chosen, listOfList)

            chosen.remove(n)
            self.combineHelper(Array, B, chosen, listOfList)

            Array.insert(0, n)

    def combine(self, A, B):
        chosen = []
        listOfList = []
        Array = list(range(1,A+1))
        self.combineHelper(Array, B, chosen, listOfList)
        return sorted(listOfList)
        return sorted(listOfList)

s = Solution()
print(s.combine(4, 2))