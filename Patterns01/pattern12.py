class Solution:
    # Function to print the pattern
    def pattern12(self, N):
        # Initial number of spaces in the first row
        spaces = 2 * (N - 1)

        # Outer loop for rows
        for i in range(1, N + 1):

            # Print increasing numbers
            for j in range(1, i + 1): 
                print(j, end="")

            # Print spaces
            for j in range(1, spaces + 1):
                print(" ", end="")

            # Print decreasing numbers
            for j in range(i, 0, -1):
                print(j, end="")

            # Move to next line
            print()

            # Reduce spaces by 2
            spaces -= 2


# Driver code
sol = Solution()
N = 5
sol.pattern12(N)