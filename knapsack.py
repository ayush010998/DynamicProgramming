"""


0/1 Knapsack Problem

We are given N items where each item has some weight and profit associated with it. We are also given a bag with capacity W, [i.e., the bag can hold at most W weight in it]. The target is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 


"""
def knapsack(self,W,wt,val,N):
    def solve(n,cap):
        if n==0 or cap==0:
            return 0
        else:
            cwt=wt[n-1]
            cv=val[n-1]
            if cwt<=cap:
                c1=cv+solve(n-1,cap-cwt)
                c2=solve(n-1,cap)
                return max(c1,c2)
            else:
                return 0+solve(n-1,cap)
    return solve(N,W)
        
