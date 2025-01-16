class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = pre[i] + nums[i];
        }

        for (int i = 0; i < n; ++i) {
            int left = pre[i];
            int right = pre.back() - pre[i + 1];
            if (left == right) {
                return i;
            }
        }
        return -1;
        
    }
};

// 0 1 8 11 17 22 28

// 0 1 3 6

// 0 2 3 2