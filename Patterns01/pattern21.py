class Solution:
    # Function to print hollow square pattern
    def pattern21(self, n):
        # Outer loop for rows
        for i in range(n):
            # Inner loop for columns
            for j in range(n):
                # Print star if it's a border cell
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*", end="")
                # Print space otherwise
                else:
                    print(" ", end="")
            # Move to next line after each row
            print()


if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Define N
    N = 4
    # Call pattern function
    sol.pattern21(N)
