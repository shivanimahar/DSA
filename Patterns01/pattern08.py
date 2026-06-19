class solution:
    def pattern7(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end = "")
            for j in range(2*n-(2*i+1)):
                print("*", end = "")
            for j in range(i):
                print(" ",end = "")
            print()
sol = solution()
n = 5
sol.pattern7(n)
              