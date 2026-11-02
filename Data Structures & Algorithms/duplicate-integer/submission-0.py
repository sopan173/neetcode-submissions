class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] > 1:
                return True
        return False