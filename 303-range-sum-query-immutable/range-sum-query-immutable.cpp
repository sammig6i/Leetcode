class NumArray {
private:
    vector<int> arr;
    vector<int> prefix;

public:
    NumArray(vector<int>& nums) {
        int n = nums.size();
        arr = nums;
        prefix = {nums[0]};
        for (int i = 1; i < n; ++i) {
            prefix.push_back(prefix.back() + nums[i]);
        }
    }
    
    int sumRange(int left, int right) {
        return prefix[right] - prefix[left] + arr[left];
    }
};
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */