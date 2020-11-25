#14. Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct.
def int_duplicate(array_nums):
    nums_set = set(array_nums)
    return len(array_nums) != len(nums_set)
print(int_duplicate([1, 2, 3, 4, 5]))
print(int_duplicate([1, 2, 3, 4, 4]))
print(int_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5]))
