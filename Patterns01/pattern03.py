class solution:
    def pattern3(self,N):
        for i in range(N+1):
            for j in range(1,i+1):
                print(j,end = " ")
            print()

if __name__ == "__main__":
    sol = solution()
    N = 5
    sol.pattern3(N)
