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
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* slow = dummy;
        ListNode* fast = head;

        while (fast && fast->next) {
            if (fast->next->val == fast->val) {
                while (fast->next && fast->next->val == fast->val) {
                    fast = fast->next;
                }

                slow->next = fast->next;
                fast = slow->next;
            } else {
                fast = fast->next;
                slow = slow->next;
            }
        }

        return dummy->next;
    }
};