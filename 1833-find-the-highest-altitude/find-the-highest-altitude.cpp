class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int res = 0, total = 0;
        for (int val : gain) {
            total += val;
            res = max(res, total);
        }
        return res;
    }
};