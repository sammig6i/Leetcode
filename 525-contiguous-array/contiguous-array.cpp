class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size(), res = 0, count = 0;
        vector<int> diff(2 * n + 1, INT_MIN);
        diff[n] = -1;

        for (int i = 0; i < n; ++i) {
            count += nums[i] == 1 ? 1 : -1;
            if (diff[count + n] >= -1) {
                res = max(res, i - diff[count + n]);
            } else {
                diff[count + n] = i;
            }
        }

        return res;
    }
};