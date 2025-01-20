class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> mp;
        unordered_set<int> freq;
        for (int num : arr) {
            mp[num]++;
        }

        for (const auto& [k, v] : mp) {
            if (freq.contains(v)) {
                return false;
            }
            freq.insert(v);
        }

        return true;

    }
};