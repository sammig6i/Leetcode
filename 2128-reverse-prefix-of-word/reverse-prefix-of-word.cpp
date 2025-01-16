class Solution {
public:
    string reversePrefix(string word, char ch) {
        for (int i = 0, j = 0; j < word.size(); ++j) {
            if (word[j] == ch) {
                int reverseIdx = j;
                for (; reverseIdx > i; --reverseIdx) {
                    char tmp = word[reverseIdx];
                    word[reverseIdx] = word[i];
                    word[i] = tmp;
                    ++i;
                }
                break;
            }
        }
        return word;
    }
};