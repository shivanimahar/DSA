class solution:
    def pattern3(self,N):
        for i in range(0,N):
            ch = chr(65+i)
            for j in range(i+1):
                print(ch,end=" ")
            print()

if __name__ == "__main__":
    sol = solution()
    N = 5
    sol.pattern3(N)
