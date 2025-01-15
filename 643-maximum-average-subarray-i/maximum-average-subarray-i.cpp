class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double curr = 0, res;
        for (int i = 0; i < k; ++i) {
            curr += nums[i];
        }

        res = curr;
        for (int i = k; i < nums.size(); ++i) {
            curr += (nums[i] - nums[i - k]);
            res = max(res, curr);
        }

        return res / k;
    }
};