class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> mp;
        string res = "";
        vector<pair<int, char>> freq;
        for (char c : s) {
            mp[c]++;
        }

        for (auto [c, count] : mp) {
            freq.push_back({count, c});
        }

        sort(freq.begin(), freq.end());
        reverse(freq.begin(), freq.end());
        
        for (auto pair : freq) {
            res += string(pair.first, pair.second);
        }

        return res;       

    }
};