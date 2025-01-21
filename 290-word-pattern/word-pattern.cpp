class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> char_to_word;
        unordered_map<string, char> word_to_char;

        vector<string> words;
        istringstream stream(s);
        string word;
        while (stream >> word) {
            words.push_back(word);
        }

        if (words.size() != pattern.size()) {
            return false;
        }

        for (int i = 0; i < pattern.size(); ++i) {
            char c = pattern[i];
            string w = words[i];
            
            if (char_to_word.find(c) != char_to_word.end() && char_to_word[c] != w or
                word_to_char.find(w) != word_to_char.end() && word_to_char[w] != c) {
                    return false;
                }

            char_to_word[c] = w;
            word_to_char[w] = c;
        }

        return true;
    }
};