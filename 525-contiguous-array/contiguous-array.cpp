class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int zero = 0, one = 0, res = 0;
        int n = nums.size();
        unordered_map<int, int> mp;

        for (int i = 0; i < n; ++i) {
            if (nums[i] == 1) {
                one++;
            } else {
                zero++;
            }

            if (mp.find(one - zero) == mp.end()) {
                mp[one - zero] = i;
            }

            if (one == zero) {
                res = one + zero;
            } else {
                int idx = mp[one - zero];
                res = max(res, i - idx);
            }
        }
        return res;
    }
};