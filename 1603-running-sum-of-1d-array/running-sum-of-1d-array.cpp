class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> pre = {nums[0]};
        for (int i = 1; i < nums.size(); ++i) {
            pre.push_back(pre.back() + nums[i]);
        }
        return pre;
    }
};