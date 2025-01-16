class Solution {
public:
    int maxVowels(string s, int k) {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int curr = 0, res = 0;
        int n = s.size();
        for (int i = 0, j = 0; j < n; ++j){
            if (vowels.find(s[j]) != vowels.end()) {
                curr++;
            }

            while (j - i + 1 > k) {
                if (vowels.find(s[i]) != vowels.end()) {
                    curr--;
                }
                ++i;
            }

            res = max(res, curr);
        }
        return res;
    };
};