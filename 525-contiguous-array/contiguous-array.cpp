class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int one = 0, zero = 0, res = 0;
        int n = nums.size();
        unordered_map<int, int> diff_idx;

        for (int i = 0; i < n; ++i) {
            if (nums[i] == 1) {
                one++;
            } else {
                zero++;
            }

            int diff = one - zero;
            if (diff_idx.find(diff) == diff_idx.end()) {
                diff_idx[diff] = i;
            }

            if (one == zero) {
                res = one + zero;
            } else {
                int idx = diff_idx[diff];
                res = max(res, i - idx);
            }
        }
        return res;
    }
};