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
        int pos = 0;
        return rec(head, n, pos);
    }

private:
    ListNode* rec(ListNode* head, int n, int& pos) {
        if (!head) {
            return nullptr;
        }

        head->next = rec(head->next, n, pos);
        pos++;
        if (pos == n) {
            return head->next;
        }
        return head;
    }

};