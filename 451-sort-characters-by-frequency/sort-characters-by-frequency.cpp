class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> mp;
        string res = "";
        for (char c : s) {
            mp[c]++;
        }

        vector<pair<int, char>> freq;
        for (auto& [k, v] : mp) {
            freq.push_back({v, k});
        }

        sort(freq.begin(), freq.end());

        for (int i = freq.size() - 1; i >= 0; --i) {
            for (int j = 0; j < freq[i].first; ++j) {
                res += freq[i].second;
            }
        }

        return res;
    }
};