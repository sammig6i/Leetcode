class Solution {
public:
    bool checkIfPangram(string sentence) {
        int seen = 0;
        for (char c : sentence) {
            int curr = c - 'a';
            int masked_bit = 1 << curr;
            seen |= masked_bit; 
        }

        return (seen == (1 << 26) - 1);
    }
};