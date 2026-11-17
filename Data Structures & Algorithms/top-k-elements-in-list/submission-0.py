class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = [[-count, num]  for num, count in Counter(nums).items()]

        heapq.heapify(count)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(count)[1])
        return res
        