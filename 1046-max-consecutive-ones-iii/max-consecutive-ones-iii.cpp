class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int L = 0, res = 0;
        for (int R = 0; R < nums.size(); ++R) {
            int n = nums[R];
            k -= 1 - n;
            if (k < 0) {
                k += 1 - nums[L];
                L++;
            } else {
                res = max(res, R - L + 1);
            }
        }
        return res;
    }
};