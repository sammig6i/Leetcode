class StockSpanner {
public:
    stack<int> st;
    unordered_map<int, int> mp;
    int idx;
    
    StockSpanner() : idx(0){
        
    }
    
    int next(int price) {
        while (!st.empty() && st.top() <= price) st.pop();


        mp[price] = idx;
        int res = st.empty() ? idx + 1 : idx - mp[st.top()];
        st.push(price);
        ++idx;
        return res;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */