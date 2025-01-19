class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) {
            return 0;
        }
        int res = 0, L = 0;
        unordered_map<char, int> counts;

        for(int R = 0; R < s.size(); ++R) {
            char c = s[R];
            counts[c]++;

            while (counts[c] > 1) {
                counts[s[L]]--;
                if (!counts[s[L]]) {
                    counts.erase(s[L]);
                }
                L++;
            }

            res = max(res, R - L + 1);
        }

        return res;

    }
};