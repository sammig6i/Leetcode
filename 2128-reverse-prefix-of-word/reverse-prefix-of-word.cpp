class Solution {
public:
    string reversePrefix(string word, char ch) {
        for (int i = 0, j = 0; j < word.size(); ++j) {
            if (word[j] == ch) {
                int L = i;
                int R = j;
                while (L < R) {
                    char tmp = word[L];
                    word[L] = word[R];
                    word[R] = tmp;
                    ++L;
                    --R;
                }
                break;
            }
        }
        return word;
    }
};