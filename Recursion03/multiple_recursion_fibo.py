# # fibionacci series (dynamic programming (bottom up approach))
# # Smaller subproblems are solved first and used to compute larger ones.
# # No recursion is used.
# def fibonacci(n):
#     if n == 0:
#         print(0)
#     elif n == 1:
#         print("0 1")
#     else:
#         fib = [0] * (n+1)
#         fib[0] = 0
#         fib[1] = 1

#         for i in range(2,n+1):
#             fib[i] = fib[i-1] + fib[i-2]
#         print(f"The Fibonacci Series up to {n}th term:")
#         print(" ".join(str(num) for num in fib))
#         #join() only works with strings, so num is list we are comverting this list into str 
#         #so that the str can be joined with " " to each other

# n = int(input("Enter n: "))
# fibonacci(n)

# # TC = O(n)
# # SC = O(n)

#Multiple recursion
# We are finding the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        last = fibonacci(n-1)
        s_last = fibonacci(n-2)
        return last + s_last
        #F(n) = F(n−1) + F(n−2)
n = int(input("Enter n: "))
print(fibonacci(n))
# TC = O(2ⁿ) --> (Har node se lagbhag 2 branches nikal rahi hain)
#                (Recursive call tree exponentially grow karta hai)

# SC = O(n)