class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> num_set;
        for (int n : nums) {
            if (num_set.contains(n)) {
                return true;
            }
            num_set.insert(n);
        }
        return false;
    }
};