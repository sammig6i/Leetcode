class Solution {
public:
    string makeGood(string s) {
        string res = "";
        for (char c : s) {
            if (!res.empty() && tolower(c) == tolower(res.back())) {
                if (isupper(c) && islower(res.back())) {
                    res.pop_back();
                } else if (islower(c) && isupper(res.back())) {
                    res.pop_back();
                } else {
                    res += c;
                }
            } else {
                res += c;
            }
        }
        return res;
    }
};