class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for num, value in enumerate(nums):
            if (target - value) in seen:
                return [seen[target - value] , num]
            seen[value] = num
        return []

        