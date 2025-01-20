class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> mp;
        for (const auto& route : paths) {
            string start = route[0];
            string dest = route[1];

            mp[start] = dest;
        }

        string start = paths[0][0];
        while (mp.find(start) != mp.end()) {
            start = mp[start];
        }

        return start;

    }
};