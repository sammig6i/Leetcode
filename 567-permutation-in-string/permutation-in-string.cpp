class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()) {
            return false;
        }

        unordered_map<char, int> s1_cnt;
        for (char c : s1) {
            s1_cnt[c]++;
        }

        int L = 0;
        unordered_map<char, int> s2_cnt;
        for (int R = 0; R < s2.size(); ++R) {
            s2_cnt[s2[R]]++;
            if ((R - L + 1) > s1.size()) {
                s2_cnt[s2[L]]--;
                if (!s2_cnt[s2[L]]) {
                    s2_cnt.erase(s2[L]);
                }
                L++;
            }

            if (s2_cnt == s1_cnt) {
                return true;
            }
        }

        return false;
    }
};