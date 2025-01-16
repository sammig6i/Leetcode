class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int curr = 0, res = INT_MAX;
        for (int i = 0, j = 0; j < nums.size(); ++j) {
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