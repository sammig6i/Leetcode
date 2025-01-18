class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> mp;
        int one = 0, zero = 0, res = 0;

        for(int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            if (n == 1) {
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