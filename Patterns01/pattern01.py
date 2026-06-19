class Solution:
    def pattern1(self,N):
        for i in range(N):
            for j in range(N):
                print("*",end=" ")
            print()
if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern1(N)