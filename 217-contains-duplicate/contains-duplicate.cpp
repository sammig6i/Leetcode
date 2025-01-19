class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int mn = INT_MAX;
        int mx = INT_MIN;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] < mn || nums[i] > mx) {
                mn = min(mn, nums[i]);
                mx = max(mx, nums[i]);
                continue;
            }
            for (int j = 0; j < i; ++j) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};