class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int res = INT_MAX;
        string balloon = "balloon";
        unordered_map<char, int> balloon_mp;
        unordered_map<char, int> mp;
        for (char c : balloon) {
            balloon_mp[c]++;
        }

        for (char c : text) {
            if (balloon_mp.find(c) != balloon_mp.end()) {
                mp[c]++;
            }
        }

        for (const auto& [c, freq] : balloon_mp) {
            if (mp.find(c) == mp.end()) {
                return 0;
            } else {
                res = min(res, mp[c] / freq);
            }
        }

        return res;
    }
};