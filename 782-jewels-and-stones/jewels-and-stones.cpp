class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res = 0;
        unordered_map<char, int> jewel_cnt;
        for (char j : jewels) {
            jewel_cnt[j]++;           
        }

        for (char s : stones) {
            if (jewel_cnt.find(s) != jewel_cnt.end()) {
                res++;
            }
        }
        return res;
    }
};