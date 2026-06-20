def palindrome(n):
    revNum = 0
    dup = n #used to compare with rev num
    while(n>0):
        ld = n%10
        revNum = (revNum * 10) + ld
        n = n//10
    return dup == revNum # Return True if they are equal, otherwise False
num = 4554
if palindrome(num):  # Check if the number is a palindrome
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")