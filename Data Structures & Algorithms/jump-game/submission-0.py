class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = 0
        for idx, num in enumerate(nums):
            if max_dist < idx:
                return False
            max_dist = max(max_dist, idx + num)
        return True
            