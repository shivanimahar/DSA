class solution():
    def pattern10(self,n):
        for i in range(1,n+1):
            print("*"*i)
        for i in range(n-1,0,-1):
            print("*" * i)
        print()
sol = solution()
n = 5
sol.pattern10(n)