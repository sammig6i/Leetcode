class Solution {
private:
    int findAns(vector<int>& nums, int goal) {
        int L = 0, R = 0, curr = 0, res = 0;
        int n = nums.size();

        while (R < n) {
            if (goal < 0) {
                return 0;
            }
            curr += nums[R];
            while (curr > goal) {
                curr -= nums[L];
                L++;
            }
            res += R - L + 1;
            R++;
        }
        return res;
    }


public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int res = findAns(nums, goal) - findAns(nums, goal-1);
        return res;
    }
};
