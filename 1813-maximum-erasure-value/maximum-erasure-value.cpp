class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0, L = 0;
        for (int R = 0; R < nums.size(); ++R) {
            mp[nums[R]]++;
            while (mp[nums[R]] > 1) {
                mp[nums[L]]--;
                if (!mp[nums[L]]) mp.erase(nums[L]);
                L++;
            }

            int sum = 0;
            for (const auto& [n, count] : mp) {
                sum += n;
            }

            res = max(res, sum);
        }
        return res;
    }
};