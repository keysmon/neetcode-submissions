class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n

        prefix_max[0] = height[0]
        for i in range(1,n):
            prefix_max[i] = max(prefix_max[i-1], height[i])
        
        suffix_max[-1] = height[-1]
        for j in range(n-2,-1,-1):
            suffix_max[j] = max(suffix_max[j+1], height[j])

        res = 0
        for i in range(1,n-1):
            res += min(prefix_max[i],suffix_max[i]) -height[i]
        return res
        
 