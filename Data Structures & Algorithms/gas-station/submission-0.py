class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        res = 0
        total = 0
        for i in range(n):
            new_total = total + gas[i] - cost[i]
            if new_total < 0:
                res = i + 1
                total = 0
            else:
                total = new_total
        return res