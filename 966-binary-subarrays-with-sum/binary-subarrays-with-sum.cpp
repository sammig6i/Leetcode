class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int, int> mp;
        mp[0] = 1;
        int res = 0, curr = 0;
        for (int n : nums) {
            curr += n;
            res += mp[curr - goal];
            mp[curr]++;
        }
        return res;
    }
};