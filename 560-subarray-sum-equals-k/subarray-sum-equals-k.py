class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0 : 1} # key=sum, value=count of sum
        curr_sum = 0
        count = 0
        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        return count
        
            
# 1 2 3
# k = 3
# sum = 3
# prefix_sums {-2: 1, 0: 1, 3: 1}
# count = 