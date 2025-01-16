class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0, j = 0, curr = 0, res = INT_MAX;
        int n = nums.size();
        while (j < n) {
            curr += nums[j++];
            if (curr >= target) {
                while (curr >= target) {
                    curr -= nums[i];
                    ++i;
                }
                res = min(res, j - i + 1);
            }
        }
        return (res == INT_MAX) ? 0 : res;
    }
};