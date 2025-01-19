class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() > magazine.size()) {
            return false;
        }

        unordered_map<char, int> mag;
        for (char& c : magazine) {
            mag[c - 'a']++;
        }

        unordered_map<char, int> ran;
        for (char& c : ransomNote) {
            ran[c - 'a']++;
        }

        for (const auto& [c, count] : ran) {
            mag[c] -= count;
            if (mag[c] < 0) {
                return false;
            }
        }
        return true;
    }
};