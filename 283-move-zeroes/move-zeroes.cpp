class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int i = 0, j = 0; j < nums.size(); ++j) {
            if (nums[j] != 0) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                ++i;
            }
        }
    }
};