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
    ListNode* cur;
    bool rec(ListNode* node) {
        if (node != nullptr) {
            if (!rec(node->next)) {
                return false;
            }
            if (cur->val != node->val) {
                return false;
            }
            cur = cur->next;
        }
        return true;
    }

public:
    bool isPalindrome(ListNode* head) {
        cur = head;
        return rec(head);
    }
};