class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res = 0;
        unordered_map<char, int> jewel_cnt;
        for (char j : jewels) {
            jewel_cnt[j]++;           
        }
        unordered_map<char, int> stone_cnt;
        for (char s : stones) {
            stone_cnt[s]++;
        }

        for (auto& [s, count] : stone_cnt) {
            if (jewel_cnt.find(s) != jewel_cnt.end()) {
                res += count;
            }
        }
        return res;
    }
};