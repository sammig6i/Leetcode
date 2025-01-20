class Solution {
public:
    bool isPathCrossing(string path) {
        unordered_map<char, pair<int, int>> direc = {
            {'N', {0, 1}},
            {'S', {0, -1}},
            {'E', {1, 0}},
            {'W', {-1, 0}}
        };
        int x = 0, y = 0;
        set<pair<int, int>> visited;
        for (char c : path) {
            visited.insert({x, y});
            pair<int, int> dir = direc[c];
            x += dir.first;
            y += dir.second;

            if (visited.contains({x, y})) {
                return true;
            }
        }

        return false;
    }
};