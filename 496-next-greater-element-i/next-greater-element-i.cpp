class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        unordered_map<int, int> mp;
        for (int i = 0; i < n; ++i) {
            mp[nums1[i]] = i;
        }

        vector<int> res(n, -1);
        stack<int> st;
        int idx;
        for (int i = 0; i < nums2.size(); ++i) {
            int num = nums2[i];
            while (!st.empty() && num > st.top()) {
                if (mp.find(st.top()) != mp.end()) {
                    idx = mp[st.top()];
                    res[idx] = num;
                }
                st.pop();
            }

            st.push(nums2[i]);
        }

        return res;

    }
};