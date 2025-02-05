class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        for (int i = 0; i < path.size(); ++i) {
            if (path[i] == '/') {
                continue;
            }

            string tmp;
            while (i < path.size() && path[i] != '/') {
                tmp += path[i];
                ++i;
            }

            if (tmp == "..") {
                if (!st.empty()) {
                    st.pop();
                }
            } else if (tmp == ".") {
                continue;
            } else {
                st.push(tmp);
            }
        }

        if (st.empty()) {
            return "/";
        }

        string res;
        while (!st.empty()) {
            res = '/' + st.top() + res;
            st.pop();
        }

        return res;
    }
};