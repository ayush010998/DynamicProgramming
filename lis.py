def longestincreasingsubsequence(self,arr,n):
    dp={}
    def solve(arr,n,li):
        if n==0:
            return 0
        elif (n,li) in dp:
            return dp[(n,li)]
        else:
            if li==-1 or arr[n-1]<arr[li]:
                c1=1+solve(arr,n-1,n-1)
                c2=solve(arr,n-1,li)
                c=max(c1,c2)
            else:
                c=solve(arr,n-1,li)
            dp[(n,li)]=c
            return c
    return solve(arr,n,-1)

            