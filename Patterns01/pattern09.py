class solution:
    def erect_pyramid(self,n):
        for i in range(n):
            print(" " * (n-i-1),end="")
            print("*" * (2*i + 1),end = "")
            print(" " * (n-i-1))
    def inverted_pyramid(self,n):
        for i in range(n):
            print(" " * i,end = "")
            print("*"*(2 * n - (2 * i + 1)), end="")
            print(" " * i)
            
sol = solution()
n = 5
sol.erect_pyramid(n)
sol.inverted_pyramid(n)
