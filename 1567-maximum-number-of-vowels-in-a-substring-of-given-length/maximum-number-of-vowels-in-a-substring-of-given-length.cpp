class Solution {
public:
    int maxVowels(string s, int k) {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int count = 0, res = 0;
        for (int i = 0, j = 0; j < s.size(); ++j) {
            if (vowels.find(s[j]) != vowels.end()) {
                count++;
            }

            while (j - i + 1 > k) {
                if (vowels.find(s[i]) != vowels.end()) {
                    count--;
                }
                ++i;
            }

            res = max(count, res);
        }

        return res;
    }
};