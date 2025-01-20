class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> mp;
        multimap<int, char> r;
        for (char c : s) {
            mp[c]++;
        }

        for (auto [k, v] : mp) {
            r.insert({v, k});
        }

        string res = "";
        for (auto it = r.rbegin(); it != r.rend(); ++it) {
            res += string(it->first, it->second);
        }
        return res;
    }
};