class Solution:
    def pattern5(self,n):
        for i in range(1,n+1):
            for j in range(1,n-i+2):
                print(j,end="")
            print()
if __name__ =="__main__":
    sol = Solution()
    n = 5
    sol.pattern5(n)

# class Solution:
#     def pattern5(self,n):
#         for i in range(n,0,-1):
#             for j in range(i):
#                 print(i,end="")
#             print()
# if __name__ =="__main__":
#     sol = Solution()
#     n = 5
#     sol.pattern5(n)
