class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> mp;
        for (char c : s) {
            mp[c]++;
        }

        string res = "";
        for (char c : order) {
            if (mp.find(c) != mp.end()) {
                res += string(mp[c], c);
                mp.erase(c);
            }   
        
        }

        for (auto& [c, count] : mp) {
            res += string(count, c);
        }

        return res;
    }
};