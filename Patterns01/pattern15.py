class solution:
    def pattern3(self,N):
        for i in range(0,N):
            for j in range(N-i):
                print(chr(65+j),end=" ")
            print()

if __name__ == "__main__":
    sol = solution()
    N = 5
    sol.pattern3(N)
