class solution:
    def getDivisors(self,n):
        res = []
        for i in range(1,n+1):
            if(n%i)==0:
                res.append(i)
        return res
sol = solution()
n=36
result = sol.getDivisors(n)

print("Divisors of", n, ":", *result)