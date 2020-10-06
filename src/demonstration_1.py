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

    # Your code here

    """
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.
Example:
Input: [1,3,3,2,1]
Output: True
Example:
Input: [0,1,2,3]
Output: False
*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""
# def contains_duplicate(nums):
#     # Your code here
#     # Plan1:
#     # made a set
#     # if set length wasn't equal to the original array length: that means there were duplicates
#     # Runtime: 0(n)
#     # Space: 0(n)
#     nums_set = set(nums)
#     if len(nums_set) == len(nums):
#         return False
#     else:
#         return True

def contains_duplicate(nums):
    # This assumes nums is sorted
    # Overall Runtime: 0(nlogn + n) --> 0(n log n)
    nums.sort()                     # sorting is usually 0(n log n)
                                    # nums.sort() sorts it in place

    # everything below this line is 0(n)
    i = 0                           # 0(n)
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:    # 0(1)
            return True
        i += 1
    return False

print(contains_duplicate_2([1))

