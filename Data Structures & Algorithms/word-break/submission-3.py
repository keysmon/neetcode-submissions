from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(left):
            if left == len(s):
                return True
            for word in wordDict:
                if s.startswith(word,left):
                    if dfs(left+len(word)):
                        return True
            else:
                return False
                
        
        return dfs(0)  