class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> num_set(sentence.begin(), sentence.end());
        return num_set.size() == 26;
    }
};