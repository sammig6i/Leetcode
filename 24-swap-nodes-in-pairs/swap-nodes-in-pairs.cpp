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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* dummy = head->next;
        ListNode* prev = nullptr;

        while (head && head->next) {
            if (prev) {
                prev->next = head->next;
            }
            prev = head;

            ListNode* next_node = head->next->next;
            head->next->next = head;
            head->next = next_node;

            head = next_node;
        }

        return dummy;
    }
};