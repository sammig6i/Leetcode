class Solution {
public:
    int maxVowels(string s, int k) {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int res = 0;
        int n = s.size();

        vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + ((vowels.find(s[i]) != vowels.end()) ? 1 : 0);
        }

        for (int i = k; i < n + 1; ++i) {
            res = max(res, prefix[i] - prefix[i - k]);
        }

        return res;
    };
};

// 0 1 1 1 2 3 4 4 5 5