class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0, L = 0;
        unordered_map<char, int> counts;

        for(int R = 0; R < s.size(); ++R) {
            counts[s[R]]++;

            while (counts[s[R]] > 1) {
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