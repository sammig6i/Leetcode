class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int L = 0, res = 0;
        unordered_set<int> st;
        for (int R = 0; R < nums.size(); ++R) {
            while (st.contains(nums[R])) {
                res = max(res, accumulate(st.begin(), st.end(), 0));
                st.erase(nums[L]);
                L++;
            }

            st.insert(nums[R]);
        }

        res = max(res, accumulate(st.begin(), st.end(), 0));

        return res;
    }
};