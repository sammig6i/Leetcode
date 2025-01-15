class Solution {
public:
    void reverseString(vector<char>& s) {
        int L = 0, R = s.size() - 1;
        while (L < R) {
            int tmp = s[L];
            s[L] = s[R];
            s[R] = tmp;
            L++;
            R--;
        }
    }
};