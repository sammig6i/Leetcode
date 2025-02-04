class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> mp;
        stack<int> st;

        for_each(nums2.rbegin(), nums2.rend(), [&](int val) {
            while (!st.empty() && st.top() <= val) st.pop();

            mp[val] = st.empty() ? -1 : st.top();

            st.push(val);
        });

        vector<int> res(nums1.size());
        transform(nums1.begin(), nums1.end(), res.begin(), [&](int val) {
            return mp[val];
        });
        return res;
    }
};