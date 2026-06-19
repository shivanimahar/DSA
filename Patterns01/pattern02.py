class Solution:
    # Function to print Pattern 2
    def pattern2(self, N):
        # Loop for rows
        for i in range(N):
            # Print stars in each row
                print("* " * (i+1)) #* (i + 1) repeats the string.
           
if __name__ == "__main__":
    # Create solution object
    sol = Solution() #Creates an object sol of the Solution class.
    # Define N
    N = 5
    # Call pattern function
    sol.pattern2(N)
