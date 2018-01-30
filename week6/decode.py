class Solution:
  # @param A : string
  # @return an integer
    def numDecodings(self, A):
        A=list(A)
        n=len(A)
        x=[0]*(n+1);
        x[0]=1;
        x[1]=1
        if(A[0]=='0'):
            return 0
        for i in range(1,n):
            if(int(A[i-1]+A[i])<=26 and int(A[i-1]+A[i])>0):
                f=1
            else:
                f=0
            if(A[i]=='0'):
                x[i+1]=x[i-1]*f
                if(x[i+1]==0):
                    x[n]=0
                    break
                x[i]=0
            else:
                x[i+1]=x[i]+x[i-1]*f
        return x[n]