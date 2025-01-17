class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int res = INT_MAX;
        unordered_set<char> balloon = {'b', 'a', 'l', 'o', 'n'};
        unordered_map<char, int> mp;
        for (char c : text) {
            if (balloon.contains(c)) {
                mp[c]++;
            }
        }

        if (mp.size() < 5) return 0;

        mp['l'] /= 2;
        mp['o'] /= 2;

        for (const auto& [c, freq] : mp) {
            res = min(res, freq);
        }

        return res;
        
    }
};