class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()) {
            return false;
        }

        vector<int> s1_cnt(26, 0);
        vector<int> s2_cnt(26, 0);
        int matches = 0;

        for (int i = 0; i < s1.size(); ++i) {
            s1_cnt[s1[i] - 'a']++;
            s2_cnt[s2[i] - 'a']++;
        }

        for (int i = 0; i < 26; ++i) {
            matches += s1_cnt[i] == s2_cnt[i] ? 1 : 0;
        }

        int L = 0;
        for (int R = s1.size(); R < s2.size(); ++R) {
            if (matches == 26) {
                return true;
            }
            char c = s2[R];
            int idx = c - 'a';
            s2_cnt[idx]++;
            if (s1_cnt[idx] == s2_cnt[idx]) {
                matches++;
            } else if (s1_cnt[idx] + 1 == s2_cnt[idx]) {
                matches--;
            }

            c = s2[L];
            idx = c - 'a';
            s2_cnt[idx]--;
            if (s1_cnt[idx] == s2_cnt[idx]) {
                matches++;
            } else if (s1_cnt[idx] - 1 == s2_cnt[idx]) {
                matches--;
            }

            L++;
        }

        return matches == 26 ? true : false;

    }
};