class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int L = 0, R = 0;
        int res = 0;
        unordered_map<int, int> mp;
        int n = nums.size();

        while(R < n) {
            mp[nums[R]]++;
            while (mp[nums[R]] > k) {
                mp[nums[L]]--;
                L++;
            }

            res = max(res, R - L + 1);
            R++;
        }

        return res;
    }
};