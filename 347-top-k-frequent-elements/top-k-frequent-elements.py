class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()

        res = []
        for c, n in arr[::-1]:
            res.append(n)
            if len(res) == k:
                return res