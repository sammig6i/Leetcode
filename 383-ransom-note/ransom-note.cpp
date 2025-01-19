class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() > magazine.size()) {
            return false;
        }

        unordered_map<char, int> ransom_count;
        for (char c : ransomNote) {
            ransom_count[c]++;
        }

        unordered_map<char, int> magazine_count;
        for (char c : magazine) {
            magazine_count[c]++;
        }

        for (const auto& [c, count] : ransom_count) {
            if (magazine_count.find(c) == magazine_count.end() || 
                magazine_count[c] < count) {
                return false;
            }
        }

        return true;

    }
};