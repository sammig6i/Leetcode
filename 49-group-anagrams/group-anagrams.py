class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)

        for s in strs:
            sorted_word = ''.join(sorted(s))
            wordMap[sorted_word].append(s)
        return wordMap.values()