class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    #    map = {}
    #    for num in nums:
    #        map[num] = map.get(num, 0) + 1
    #        if map[num] > 1: 
    #           return True
    #    return False
    # use Set instead of map

