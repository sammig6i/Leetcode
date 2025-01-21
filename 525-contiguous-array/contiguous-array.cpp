class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size(), count = 0, res = 0;
        vector<int> arr(2 * n + 1, INT_MIN);
        arr[n] = -1;

        for (int i = 0; i < nums.size(); ++i) {
            count += nums[i] == 1 ? 1 : -1;
            if (arr[count + n] >= -1) {
                res = max(res, i - arr[count + n]);
            } else {
                arr[count + n] = i;
            }
            
        }

        return res;
    }
};