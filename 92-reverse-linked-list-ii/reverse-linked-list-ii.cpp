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
        ListNode* left_node = head;
        ListNode* first_node = dummy;

        for (int i = 1; i < left; ++i) {
            left_node = left_node->next;
            first_node = first_node->next;
        }

        ListNode* prev = nullptr;
        for (int i = 0; i < (right - left + 1); ++i) {
            ListNode* next = left_node->next;
            left_node->next = prev;
            prev = left_node;
            left_node = next;
        }

        first_node->next->next = left_node;
        first_node->next = prev;

        return dummy->next;        
    }
};
