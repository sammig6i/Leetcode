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
        for _ in range(k):
            res.append(arr.pop()[1])
        return res