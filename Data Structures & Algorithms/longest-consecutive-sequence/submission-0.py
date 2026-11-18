class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        for num in nums:
            if num - 1 in numSet:
                continue
            cur_len = 1
            while cur_len + num in numSet:
                cur_len += 1
            res = max(res, cur_len)
        return res
