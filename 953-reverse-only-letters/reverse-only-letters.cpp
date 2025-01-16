class Solution {
public:
    string reverseOnlyLetters(string s) {
        for (int i = 0, j = s.size() - 1; i < j;) {
            if (!isalpha(s[i])) {
                ++i;
            } else if (!isalpha(s[j])) {
                --j;
            } else {
                char tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
                ++i;
                --j;
            }
        }

        return s;
    }
};