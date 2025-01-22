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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        for (int i = 0; i < left - 1; ++i) {
            prev = prev->next;
        }

        ListNode* sublist_head = prev->next;
        ListNode* sublist_tail = sublist_head;
        for (int i = 0; i < right - left; ++i) {
            sublist_tail = sublist_tail->next;
        }
        ListNode* next = sublist_tail->next;
        sublist_tail->next = nullptr;
        prev->next = reverseList(sublist_head);
        sublist_head->next = next;
        return dummy->next;

    }
private:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* curr = head;
        ListNode* prev = nullptr;

        while (curr) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;
    }
};