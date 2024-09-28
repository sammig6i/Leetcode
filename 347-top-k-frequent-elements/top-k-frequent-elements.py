class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for i, c in count.items():
            freq[c].append(i)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for i in freq[i]:
                res.append(i)
                if len(res) == k:
                    return res

        
