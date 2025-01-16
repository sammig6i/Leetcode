class Solution {
public:
    int maxVowels(string s, int k) {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int n = s.size(), res = 0;
        vector<int> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = pre[i] + (vowels.find(s[i]) != vowels.end() ? 1 : 0);
        }

        for (int i = k; i < n + 1; ++i) {
            res = max(res, pre[i] - pre[i - k]);
        }

        return res;
    };
};