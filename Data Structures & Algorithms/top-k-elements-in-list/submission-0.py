import heapq 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #v1 with dict sorting of counts
        #count_map = {}
        #for num in nums:
        #    count_map[num] = count_map.get(num, 0) + 1
        #count_map = dict(sorted(count_map.items(), key=lambda kv: kv[1], reverse=True))
        #return list(count_map)[:k]

        #v2 min heap with size k
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for count, num in heap:
            result.append(num)
        return result
        """
        """ v3 - """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (-count, num))
        result = []
        for _ in range(k):
            pair = heapq.heappop(heap)
            result.append(pair[1])
        return result

        

