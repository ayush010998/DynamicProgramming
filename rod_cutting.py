#problem statements :- rod of length N and an array of prices , price i denotes the value of pies of length i .Determine maximum value obtain by cutting the rod and selling?

class solution:
    def cutRod(self,price,n):
        dp={}
        def solve(cl,rl):
            if cl==0 or rl==0:
                return 0
            elif (cl,rl) in dp:
                return dp[(cl,rl)]
            else:
                val=price[cl-1]
                if cl<=rl:
                    c1=val+solve(cl,rl-cl)
                    c2=solve(cl-1,rl)
                    c=max(c1,c2)
                else:
                    c=solve(cl-1,rl)
                dp[(cl,rl)]=c
                return c
        return solve(n,n)
                