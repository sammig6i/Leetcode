class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() > magazine.size()) {
            return false;
        }

        int count[26] = {0};
        for (char c : magazine) {
            count[c - 'a']++;
        }

        for (char c : ransomNote) {
            count[c - 'a']--;
            if (count[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};