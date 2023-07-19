#longest common subsequence

dp={}
def solve(s1,s2,m,n):
    if m==0 or n==0:
        return 0
    elif (m,n) in dp:
        return dp[(m,n)]
    else:
        if s1[m-1]==s2[n-1]:
            c=1+solve(s1,s2,m-1,n-1)
        else:
            c1=solve(s1,s2,m-1,n)
            c2=solve(s1,s2,m,n-1)
            c=max(c1,c2)
        dp[(m,n)]=c
        return c
    return solve(str1,str2,x,y)
        