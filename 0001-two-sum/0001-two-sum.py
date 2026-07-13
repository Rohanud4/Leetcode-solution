class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store value -> index
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
