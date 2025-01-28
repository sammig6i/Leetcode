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
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        int d = 2;
        ListNode* prev_group = head;
        ListNode* cur = head->next;
        while (cur) {
            int sz = 0;
            ListNode* first = cur;
            ListNode* last = nullptr;
            while (cur && sz < d) {
                last = cur;
                cur = cur->next;
                ++sz;
            }

            if (sz % 2 == 0) {
                last->next = nullptr;
                prev_group->next = reverseList(first);
                first->next = cur;
                last = first;
            }
            ++d;
            prev_group = last;
        }
        return head;
    }
private:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* new_head = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return new_head;
    }
};