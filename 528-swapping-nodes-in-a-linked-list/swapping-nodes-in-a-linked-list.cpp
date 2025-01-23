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

        ListNode* cur = left;
        ListNode* right = head;
        while (cur->next) {
            cur = cur->next;
            right = right->next;
        }

        int tmp = left->val;
        left->val = right->val;
        right->val = tmp;

        return head;
    }
};