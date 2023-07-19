def maxSubarray(self,arr:list[int])->int:
    n=len(arr)
    dp=[0]*n
    dp[0]=arr[0]
    for i in range(1,n):
        c1=arr[i]
        c2=dp[i-1]+arr[i]
        dp[i]=max(c1,c2)
    return max(c1,c2)
    