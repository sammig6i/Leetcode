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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(INT_MIN);
        dummy->next = head;
        ListNode* curr = head;
        ListNode* prev = dummy;

        while (curr) {
            if (prev->val == curr->val) {
                prev->next = curr->next;
                prev = prev;
                curr = curr->next;
                continue;
            }
            prev = curr;
            curr = curr->next;
        }

        return dummy->next;



    }
};