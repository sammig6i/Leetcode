class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) {
            return 0;
        }
        int res = 0, L = 0;
        unordered_map<char, int> mp;

        for(int R = 0; R < s.size(); ++R) {
            char c = s[R];
            if (mp.find(c) != mp.end()) {
                L = max(mp[c], L);
            }


            res = max(res, R - L + 1);
            mp[s[R]] = R + 1;
        }

        return res;

    }
};