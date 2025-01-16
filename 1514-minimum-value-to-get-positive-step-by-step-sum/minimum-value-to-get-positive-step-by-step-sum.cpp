class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int min_val = 1;
        int total = 0;
        for (int num : nums) {
            total += num;
            min_val = min(min_val, total);
        }
        
        return (min_val >= 1) ? min_val : abs(min_val) + 1;
    }
};

