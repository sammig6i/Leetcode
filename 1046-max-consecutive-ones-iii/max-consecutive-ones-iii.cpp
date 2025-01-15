class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int L = 0, curr = 0, res = 0;
        for (int R = 0; R < nums.size(); ++R) {
            if (nums[R] == 0) curr++;

            while (curr > k) {
                if (nums[L] == 0) curr--;
                L++;
            }

            res = max(res, R - L + 1);
        }

        return res;
    }
};