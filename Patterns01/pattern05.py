# class Solution:
#     def pattern5(self,n):
#         for i in range(n,0,-1):
#             print("*" * i)
#         print()
# if __name__ =="__main__":
#     sol = Solution()
#     n = 5
#     sol.pattern5(n)
class solution:
    def pattern5(self,n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print("*", end = " ")
            print()
sol = solution()
n = 5
sol.pattern5(n)
            



