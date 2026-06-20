class solution:
    def revnum(self,n):
        revnum = 0
        while(n>0):
            lastdig = n%10
            revnum = revnum * 10 + lastdig
            n = n//10
        return revnum
sol = solution()
n = 987
print(sol.revnum(n))