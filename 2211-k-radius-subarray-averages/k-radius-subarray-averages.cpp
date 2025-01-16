class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int x = k * 2 + 1;
        int n = nums.size();
        vector<int> res(n, -1);

        if (n < x) return res;
        vector<long> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = pre[i] + nums[i];
        }

        for (int i = k; i < n - k; ++i) {
            long sum = pre[i + k + 1] - pre[i - k];
            int avg = sum / x;
            res[i] = avg;
        }

        return res;
    }
};