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
        int position = 0;
        return rec(head, n, position);
    }

private:
    ListNode* rec(ListNode* head, int n, int& position) {
        if (!head) {
            return nullptr;
        }

        head->next = rec(head->next, n, position);
        position++;
        if (position == n) {
            return head->next;
        }

        return head;
    }

};