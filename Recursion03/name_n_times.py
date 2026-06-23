class Solution:
    
    def printName(self,name,count,n):
        #count = 0 #writing count here will reset, count to 0 everytime

        if count == n:
            return 
        print(name) #print name

        # Recursive call with incremented count
        self.printName(name,count + 1,n)

sol = Solution()
n = 5
name = "Shivani"
sol.printName(name,0,n)
