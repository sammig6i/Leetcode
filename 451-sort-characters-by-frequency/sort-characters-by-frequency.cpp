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
        reverse(freq.begin(), freq.end());

        for (auto pair : freq) {
            res += string(pair.first, pair.second);
        }
        return res;
    }
};