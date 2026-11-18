class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        max_len = 0
        for i in range(n):
            m = 1
            while i-m>=0 and i+m<n and s[i-m] == s[i+m] :
                m += 1
            if 2*m - 1 > max_len:
                max_len = 2*m-1
                res = s[i-m+1:m+i]
        for i in range(n-1):
            m = 0
            while i-m>=0 and i+m+1<n and s[i-m] == s[i+m+1]:
                m += 1
            if 2*m  > max_len:
                max_len = 2*m
                res = s[i-m+1:i+m+1]
        return res
