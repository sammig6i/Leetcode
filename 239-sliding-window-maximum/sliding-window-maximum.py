class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        L = 0
        for R in range(len(nums)):
            while q and nums[R] > nums[q[-1]]:
                q.pop()
            q.append(R)

            if L > q[0]:
                q.popleft()

            if (R - L + 1) >= k:
                res.append(nums[q[0]])
                L += 1
        return res  



        