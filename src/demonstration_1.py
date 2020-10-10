"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified (new) `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""
def remove_duplicates(nums):
    # UPER 
    # Understand 
        # Must remove duplicates
        # the array is already sorted
        # numbers don't necessarily need to be consecutive
        # Will they all be ints?

        # length indicates the end of the array after removing duplicates (for in place solution)
        # ( in place / out place )
    # Plan
        # turn the list into a set --> automatically remove duplicates b/d that's what sets do
        # OUT OF PLACE 
        nums_set = set()                # runtime: 0(n)
        for num in nums:                # space complexity: 0(n)    
            nums_set.add(num)
        return list(nums_set)
        # turn it into a dictionary to eliminate duplicate keys -- similar to the set approach

        # loop within a loop to check each variable against the other variables.
        # use a conditional in a list comprehension? possibly?

        # IN PLACE
def remove_duplicates_in_place(nums):
    # in place means that we don't use extra space -- we have to swap / move numbers around within 'nums'
    # we can run a for loop
    # for i in range(len(nums) - 1):
    #     if nums[i] == nums[i+1]:
    #         nums.pop(i+1)
    #     # remove it from the list
    # return nums
    # overall runtime: 0(n^2)
    # space complexity: 0(1)
    i = 0
    while i < len(nums) - 1:                # how many times? 0(n)
        if nums[i] == nums[i+1]:            #0(1)
            nums.pop(i+1)                   # remove the element at the index i + 1     # 0(n)
        else: i = i + 1
        # remove it from the list
    return nums

print(remove_duplicates_in_place([0, 1, 2, 3, 3, 3, 3, 4]))


def remove_duplicates_in_place_linear(nums):
    # iterate through the list
    # keep one index pointing to the end of the part of the array with no duplicates
    non_duplicate_index = 0
    # and another index pointing to the "current" element in th earray
    for current_index in range(len(nums)):
    # if current element is already in the array, skip it.
        if nums[current_index] == nums[non_duplicate_index - 1]:
            #skip it
            continue
        else:
    # otherwise, set num[non_dupliate_index] to current element and increment non_duplicate_index
            nums[non_duplicate_index] = nums[current_index]
            non_duplicate_index += 1
    return nums, non_duplicate_index

    # [0, 1, 2, 3, 4, 3, 4]

