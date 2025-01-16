class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size(), res = INT_MAX;
        int curr = 0;
        for (int i = 0, j = 0; j < n; ++j) {
            curr += nums[j];
            while (curr >= target) {
                res = min(res, j - i + 1);
                curr -= nums[i];
                ++i;
            }
        }
        return (res == INT_MAX) ? 0 : res;
    }
};