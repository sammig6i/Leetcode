class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int min_val = INT_MAX;
        int i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j]) {
                ++i;
            } else if (nums1[i] > nums2[j]) {
                ++j;
            } else {
                min_val = min(min_val, nums1[i]);
                ++i;
                ++j;
            }
        }

        return (min_val == INT_MAX) ? -1 : min_val;
    }
};