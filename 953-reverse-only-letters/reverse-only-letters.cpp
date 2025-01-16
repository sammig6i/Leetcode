class Solution {
public:
    string reverseOnlyLetters(string s) {
        int L = 0, R = s.size() - 1;
        while (L < R) {
            if(isalpha(s[L]) && isalpha(s[R])) {
                char tmp = s[L];
                s[L] = s[R];
                s[R] = tmp;
                L++;
                R--;
            } else {
                if (!isalpha(s[L])) {
                    L++;
                }

                if (!isalpha(s[R])) {
                    R--;
                }
            }
        }
        return s;
    }
};