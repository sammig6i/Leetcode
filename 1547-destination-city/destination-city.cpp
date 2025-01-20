class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> destinations;

        for (auto& route : paths) {
            string dest = route[1];
            destinations.insert(dest);
        }

        for (auto& route : paths) {
            string begin = route[0];
            destinations.erase(begin);
        }

        unordered_set<string>::iterator res = destinations.begin();
        
        return *res;

    }
};