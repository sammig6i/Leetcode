class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> mp;
        multimap<int, char> r;
        for (char c : s) {
            mp[c]++;
        }

        vector<pair<int, char>> freq;
        for (auto [k, v] : mp) {
            freq.push_back({v, k});
        }

        sort(freq.begin(), freq.end());
        reverse(freq.begin(), freq.end());

        string res = "";
        for (auto pair : freq) {
            res += string(pair.first, pair.second);
        }
        return res;
    }
};