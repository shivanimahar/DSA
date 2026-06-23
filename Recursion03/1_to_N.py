# #1 to N using normal recursion
# class solution:
#     def printNum(self, i, n):
#         if i > n:
#             return
#         print(i,end=" ")

#         self.printNum(i + 1,n)

# sol = solution()
# n = 10
# sol.printNum(1,n)


#Using backtracking (1 to 10)
# just exchange the position of print and recursive calling lines
# (it is basically reversing the numbers,i.e.
# the actual logic we used is to print 10 - 1, but as we used print()statement 
# after recursive call, so no are revered here i.e. 1-10 it is due to backtracking)

class solution:
    def printNumbers(self,i,n):
        if i<1:
            return

        self.printNumbers(i-1,n)
        print(i,end=" ")
sol = solution()
n = 10
sol.printNumbers(n,n)
print()

# Trick:
    # print() before recursive call --> normal recursion
    # print() after recursive call --> backtracking
    
# Time Complexity = O(n)
# Space Complexity = O(n) (recursive call stack ki wajah se).


