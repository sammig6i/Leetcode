class Solution {
public:
    string reverseWords(string s) {
        int lastSpaceIdx = -1;
        string result;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            if (i == n - 1 || s[i] == ' ') {
                int reverseIdx = (i == n - 1) ? i : i - 1;
                for (; reverseIdx > lastSpaceIdx; --reverseIdx) {
                    result += s[reverseIdx];
                }

                if (i != n - 1) result += ' ';

                lastSpaceIdx = i;
            }
        }

        return result;
    }
};