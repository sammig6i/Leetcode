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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head || !head->next) {
            return nullptr;
        }

        ListNode* dummy = new ListNode(0);
        ListNode* new_head = reverseList(head);

        dummy->next = new_head;
        ListNode* curr = new_head;
        ListNode* prev = dummy;
        for (int i = 1; i < n; ++i) {
            prev = prev->next;
            curr = curr->next;
        }
// dummy 2 1
        prev->next = curr->next;
        dummy->next = reverseList(dummy->next);
        return dummy->next;
    }
private:
    ListNode* reverseList(ListNode* head) {
        if (!head | !head->next) {
            return head;
        }

        ListNode* new_head = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return new_head;
    }
};