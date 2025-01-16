class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int left_sum = 0;
        int total = accumulate(nums.begin(), nums.end(), 0);

        for (int i = 0; i < n; ++i) {
            int right_sum = total - nums[i] - left_sum;
            if (right_sum == left_sum) {
                return i;
            }
            left_sum += nums[i];
        }
        return -1;
        
    }
};