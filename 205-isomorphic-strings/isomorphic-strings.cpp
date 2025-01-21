class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, int> s_mp;
        unordered_map<char, int> t_mp;

        for (int i = 0; i < s.size(); ++i) {
            if (s_mp.find(s[i]) != s_mp.end() && s_mp[s[i]] != t[i] or
                t_mp.find(t[i]) != t_mp.end() && t_mp[t[i]] != s[i]) {
                    return false;
                }
            s_mp[s[i]] = t[i];
            t_mp[t[i]] = s[i];
        }
        return true;
    }
};