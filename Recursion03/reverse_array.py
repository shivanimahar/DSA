# #Brute force,
# class solution:
#     def reverseArray(self,arr):
#         n = len(arr)
#         rev_arr = [0] * n #Creates a new array of size n, filled with zeros.
#         # [0,0,0,0] Because we need an empty array to store reversed values.
#         for i in range(n):
#             rev_arr[i] = arr[n-i-1] #picks element from back of org arr and stores them to the front of new arr

#         return rev_arr
# sol = solution()
# arr = list(map(int, input("Enter arr: ").split()))
# result = sol.reverseArray(arr)
# print("Reversed array: ",result)

# # TC = O(n)
# # SC = O(n)

#Better approach , creating two pointer, pointing at first and at last
# class solution:
#     def reverseArray(self, arr):
#         p1 = 0
#         p2 = len(arr) - 1

#         while p1 < p2:
#             arr[p1] , arr[p2] = arr[p2] , arr[p1]

#             p1 += 1
#             p2 -= 1
#         return arr
# sol = solution()
# arr = list(map(int, input("Enter arr: ").split()))
# result = sol.reverseArray(arr)
# print("Reversed array:", result)

# TC): O(n)
# SC = O(1) Extra array is used

#Built in function

class solution:
    def reverseArray(self, arr):
        arr[:] = arr[::-1]
        #Replace all elements of arr with the reversed version of arr
        return arr
sol = solution()
arr = list(map(int, input("Enter arr: ").split()))
result = sol.reverseArray(arr)
print("Reversed array:", result)

# TC: O(n)
# SC: O(n)