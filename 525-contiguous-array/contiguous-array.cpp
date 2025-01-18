class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size(), count = 0, res = 0;
        vector<int> diff_idx(2 * n + 1, INT_MIN);
        diff_idx[n] = -1;

        for (int i = 0; i < n; ++i) {
            count += nums[i] == 1 ? 1 : -1;
            if (diff_idx[count + n] >= -1) {
                res = max(res, i - diff_idx[count + n]);
            } else {
                diff_idx[count + n] = i;
            }
        }
        return res;
    }
};