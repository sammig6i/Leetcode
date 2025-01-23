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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* left = head;
        for (int i = 0; i < k - 1; ++i) {
            left = left->next;
        }

        ListNode* fast = left;
        ListNode* right = head;
        while (fast->next) {
            fast = fast->next;
            right = right->next;
        }

        swap(left->val, right->val);
        return head;
    }
};