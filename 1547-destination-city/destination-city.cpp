class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> mp;
        for (auto route : paths) {
            mp[route[0]] = route[1];
        }

        string start = paths[0][0];
        while (mp.find(start) != mp.end()) {
            start = mp[start];
        }

        return start;
    }
};