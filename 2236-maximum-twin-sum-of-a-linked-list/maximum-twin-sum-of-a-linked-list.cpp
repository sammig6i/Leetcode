/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* slow = head, *fast = head;
        stack<int> st;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        while (slow) {
            st.push(slow->val);
            slow = slow->next;
        }

        int res = 0;
        slow = head;
        while (!st.empty()) {
            res = max(res, st.top() + slow->val);
            slow = slow->next;
            st.pop();
        }

        return res;
    }
};