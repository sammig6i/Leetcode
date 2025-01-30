class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int window_size = 2 * k + 1;
        long window_sum = 0;
        int n = nums.size();
        vector<int> res(n, -1);

        if (n < window_size) {
            return res;
        }

        for (int i = 0; i < n; ++i) {
            window_sum += nums[i];

            if (i - window_size >= 0) {
                window_sum -= nums[i - window_size];
            }

            if (i >= window_size - 1) {
                res[i - k] = window_sum / window_size;
            }
        }

        return res;
    }
};