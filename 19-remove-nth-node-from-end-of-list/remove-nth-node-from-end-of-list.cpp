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
        int N = 0;
        ListNode* curr = head;
        while (curr) {
            N++;
            curr = curr->next;
        }

        int idx = N - n;
        if (idx == 0) {
            return head->next;
        }

        curr = head;
        for (int i = 0; i < N; ++i) {
            if (i + 1 == idx) {
                curr->next = curr->next->next;
                break;
            }
            curr = curr->next;
        }

        return head;
    }
};