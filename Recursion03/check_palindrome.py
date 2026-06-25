#two pointer approch
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        #If left character has charac other than alphabet or num then move forward to check palindrome
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        #Convert both to lowercase and compare.
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

if __name__ == "__main__":
    str = "@ABCDCBA"
    #its a palindrome
    ans = is_palindrome(str)

    if ans:
        print("Palindrome")
    else:
        print("Not Palindrome")