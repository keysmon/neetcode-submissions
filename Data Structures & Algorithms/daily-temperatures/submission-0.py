class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, idx))
                continue
            while stack and temp > stack[-1][0]:
                that_number, that_idx = stack.pop()
                res[that_idx] = idx - that_idx
            stack.append([temp, idx])
        return res