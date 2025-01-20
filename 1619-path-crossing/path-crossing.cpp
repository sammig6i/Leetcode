class Solution {
public:
    bool isPathCrossing(string path) {
        set<pair<int, int>> coords;
        coords.insert({0, 0});
        int x = 0, y = 0;

        for (char d : path) {
            switch(d) {
                case 'N':
                    y++;
                    break;
                case 'S':
                    y--;
                    break;
                case 'E':
                    x++;
                    break;
                case 'W':
                    x--;
                    break;
            }
            if (coords.contains({x, y})) {
                return true;
            }
            coords.insert({x, y});
        }

        return false;
    }
};