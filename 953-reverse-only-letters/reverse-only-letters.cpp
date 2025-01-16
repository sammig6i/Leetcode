class Solution {
public:
    string reverseOnlyLetters(string s) {
        for (int i = 0, j = s.size() - 1; i < j; ++i, --j) {
            while (i < j && !isalpha(s[i])) ++i;
            while (i < j && !isalpha(s[j])) --j;
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
        }
        return s;
    }
};