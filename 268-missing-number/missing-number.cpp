class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> num_set(nums.begin(), nums.end());
        for (int i = 0; i < n + 1; ++i) {
            if (num_set.find(i) == num_set.end()) {
                return i;
            }
        }

        return -1;
    }
};