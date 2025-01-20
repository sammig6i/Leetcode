class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_set<int> st;
        int res = 0, L = 0;
        for (int R = 0; R < nums.size(); ++R) {
            while (st.contains(nums[R])) {
                st.erase(nums[L]);
                L++;
            }
            st.insert(nums[R]);
            res = max(res, accumulate(st.begin(), st.end(), 0));
        }
        return res;
    }
};