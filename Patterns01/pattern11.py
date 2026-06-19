class solution():
    def pattern11(self,n):
        for i in range(n):
            if(i%2==0):
                start = 1
            else:
                start = 0
            for j in range(i+1): #This decides how many numbers to print.(loop kitne bar chlegi ye wali)
                print(start,end="")
                start = 1 - start #(repeat hoga,inner loop mai hi)
            print()
sol = solution()
n = 5
sol.pattern11(n)
            