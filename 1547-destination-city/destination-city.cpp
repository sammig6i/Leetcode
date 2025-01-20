class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> begin;
        unordered_set<string> destinations;

        for (auto& route : paths) {
            string start = route[0];
            string dest = route[1];

            begin.insert(start);
            destinations.insert(dest);
        }

        for (string city : destinations) {
            if (begin.find(city) == begin.end()) {
                return city;
            }
        }
        return "";

    }
};