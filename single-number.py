from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # Method 1:
        # result = 0
        # for num in nums:
        #     result ^= num
        # return result
        
        # Method 2:
        for num in nums:
            if nums.count(num) == 1:
                return num

# Example usage:
nums = [4, 1, 2, 1, 2]
sol = Solution()
print(sol.singleNumber(nums))  


