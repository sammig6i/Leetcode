class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size(), res = 0, count = 0;
        vector<int> diff_idx(2 * n + 1, -2);
        diff_idx[n] = -1;

        for (int i = 0; i < n; ++i) {
            count += nums[i] == 1 ? 1 : -1;
            if (diff_idx[count + n] != -2) {
                res = max(res, i - diff_idx[count + n]);
            } else {
                diff_idx[count + n] = i;
            }
        }

        return res;
    }
};