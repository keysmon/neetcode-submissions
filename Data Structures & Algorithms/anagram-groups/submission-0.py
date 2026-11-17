class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_to_list = defaultdict(list)
        for word in strs:
            letter_count = [0] * 26
            for c in word:
                letter_count[ord(c)-ord("a")]+=1
            count_to_list[tuple(letter_count)].append(word)

        return list(count_to_list.values())