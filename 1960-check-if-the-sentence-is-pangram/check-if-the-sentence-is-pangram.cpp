class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> set;
        for (const char& s: sentence) {
            set.insert(s);
        }

        return set.size() == 26;
    }
};