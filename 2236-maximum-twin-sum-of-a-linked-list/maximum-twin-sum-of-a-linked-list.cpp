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
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* last_node = dummy;
        while (fast && fast->next) {
            slow = slow->next;
            last_node = last_node->next;
            fast = fast->next->next;
        }

        ListNode* prev = nullptr;
        while (slow) {
            ListNode* next_node = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next_node;
        }

        last_node->next = prev;
        slow = last_node->next;
        ListNode* slower = head;
        int res = 0;
        while (slow) {
            res = max(res, slow->val + slower->val);
            slow = slow->next;
            slower = slower->next;
        }

        return res;
    }
};

