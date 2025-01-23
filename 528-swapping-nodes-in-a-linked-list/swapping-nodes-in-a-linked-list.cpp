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
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* first = dummy;
        ListNode* second = dummy;
        
        for (int i = 0; i < k; ++i) {
            first = first->next;
        }

        ListNode* fast = first;
        while (fast) {
            second = second->next;
            fast = fast->next;
        }

        int tmp = second->val;
        second->val = first->val;
        first->val = tmp;

        return dummy->next;
    }
};