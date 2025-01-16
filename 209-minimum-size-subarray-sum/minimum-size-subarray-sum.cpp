class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        int res = n + 1;
        for (int i = 0; i < n; ++i) {
            int L = i, R = n;
            while (L < R) {
                int mid = (L + R) / 2;
                int curr = prefix[mid + 1] - prefix[i];
                if (curr >= target) {
                    R = mid;
                } else {
                    L = mid + 1;
                }
            }
            if (L < n) {
                res = min(res, L - i + 1);
            }
        }

        return res % (n + 1);
    }
};