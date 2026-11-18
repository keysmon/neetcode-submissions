class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            count1 = dict(Counter(s1))
            count2 = dict(Counter(s2[i:i+len(s1)]))
            for key,value in count1.items():
                if key not in count2:
                    break
                if count2[key] < value:
                    break
            else:
                return True
        return False
        