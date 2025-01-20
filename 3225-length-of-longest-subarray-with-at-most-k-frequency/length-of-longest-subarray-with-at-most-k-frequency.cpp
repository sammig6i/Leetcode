class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int L = 0, res = 0;
        unordered_map<int, int> mp;
        for (int R = 0; R < nums.size(); ++R) {
            mp[nums[R]]++;

            while (mp[nums[R]] > k) {
                mp[nums[L]]--;
                L++;
            }

            res = max(res, R - L + 1);
        }

        return res;
    }
};