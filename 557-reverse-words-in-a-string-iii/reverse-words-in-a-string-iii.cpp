class Solution {
public:
    string reverseWords(string s) {
        int lastSpaceIdx = -1;
        int n = s.size();
        for (int i = 0; i <= n; ++i) {
            if (i == n || s[i] == ' ') {
                int L = lastSpaceIdx + 1;
                int R = i - 1;
                while (L < R) {
                    char tmp = s[L];
                    s[L] = s[R];
                    s[R] = tmp;
                    L++;
                    R--;
                }
                lastSpaceIdx = i;
            }
        }

        return s;
    }
};