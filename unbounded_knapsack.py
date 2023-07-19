def knapsack(self,N,W,val,wt):
    dp={}
    def solve(n,cap):
        if n==0 or cap==0:
            return 0
        elif(n,cap) in dp:
            return dp[(n,cap)]
        else:
            cw=wt[n-1]
            cv=val[n-1]
            if cw<=cap:
                c1=cv+solve(n,cap-cw)
                c2=solve(n-1,cap)
                c=max(c1,c2)
            else:
                c=solve(n-1,cap)
            dp[(n,cap)]=c
            return c
    return solve(N,W)

#because item quantity is infinite here so we don't reduce the choice1 capacity by the chosen value.
