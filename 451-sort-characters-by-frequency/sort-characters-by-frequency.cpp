class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> mp;
        string res = "";
        for (char c : s) {
            mp[c]++;
        }

        vector<pair<char, int>> freq(mp.begin(), mp.end());

        sort(freq.begin(), freq.end(), [](const pair<char, int>& a, const pair<char, int>& b) {
            return a.second > b.second;  // Sort by value descending
        });

        for (const auto& p : freq) {
            res += string(p.second, p.first);
        }

        return res;

    }
};