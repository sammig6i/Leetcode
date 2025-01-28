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
    bool isPalindrome(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* prev = dummy;
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            prev = prev->next;
            slow = slow->next;
            fast = fast->next->next;
        }

        prev->next = nullptr;
        prev = nullptr;
        while (slow) {
            ListNode* next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next;
        }

        ListNode* cur = head;
        while(prev && cur) {
            if (prev->val != cur->val) {
                return false;
            }
            prev = prev->next;
            cur = cur->next;
        }

        return true;
    }
};