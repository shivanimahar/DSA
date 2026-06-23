
#N to 1 using normal recursion
#this is the actual logic for printing N to 1
# class solution:
#     def printNumbers(self,i,n):
#         if i<1:
#             return
#         print(i,end=" ")

#         self.printNumbers(i-1,n)
# sol = solution()
# n = 10
# sol.printNumbers(n,n)
# print()

#using backtracking, we used the actual logic to print 1 - 10 first
#then we used backtracking which make 1-10 reverse to 10-1 , so now it will print 10-1
class solution:
    def printNum(self,i,n):
        if i > n:
            return
        self.printNum(i + 1,n)  # recursive call
        print(i,end=" ")
    
sol = solution()
n = 10
sol.printNum(1,n)

# Trick:
    # print() before recursive call --> normal recursion
    # print() after recursive call --> backtracking
    
# Time Complexity = O(n)
# Space Complexity = O(n) (recursive call stack ki wajah se).
