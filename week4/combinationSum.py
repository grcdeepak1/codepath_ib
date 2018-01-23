class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return a list of list of integers
    def combinationHelper(self, C, sm, ans, r, i):
        if sm < 0:
            return
        if sm == 0:
            ans.append(sorted(r[:]))
            return
        while i <= len(C)-1 and sm - C[i] >= 0:
            r.append(C[i])
            self.combinationHelper(C, sm - C[i], ans, r, i)
            r.pop()
            i += 1

    def combinationSum(self, C, T):
        chosen =[]
        ans = []
        C = sorted(list(set(C)))
        self.combinationHelper(C, T, ans, [], 0)
        return sorted(ans)