class Solution {
public:
    bool isPathCrossing(string path) {
        set<pair<int, int>> coords;
        int x = 0, y = 0;
        coords.insert({x, y});

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