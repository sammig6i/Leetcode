class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_set<int> st;
        unordered_map<int, int> mp;
        int n = arr.size();
        for (int num : arr) {
            mp[num]++;
        }

        for (const auto& [k, v] : mp) {
            st.insert(v);
        }

        int res = accumulate(st.begin(), st.end(), 0);
        return (res == n);


    }
};