class Solution:
    # @param x : integer
    # @param y : integer
    # @param z : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return 1%d
        temp = self.pow(x, n/2, d)
        return (temp*temp)%d if n%2==0 else (x*temp*temp)%d