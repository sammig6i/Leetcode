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
private:
    ListNode* reverseList(ListNode* begin, ListNode* end) {
        ListNode* prev = begin, *cur = begin->next, *next=nullptr;
        while (cur != end) {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        return prev;
    }

public:
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* begin = head->next, *tail = head, *end = begin, *tmp = nullptr;
        for (int k = 2; ; ++k) {
            int cnt = 0;
            for (int i = 0; i < k; ++i) {
                if (!end) {
                    break;
                }

                tmp = end;
                end = end->next;
                ++cnt;
            }

            if (cnt % 2 == 0) {
                tail->next = reverseList(begin, end);
                tail = begin;
            } else {
                tail->next = begin;
                tail = tmp;
            }

            begin = end;
            if (!begin) {
                tail->next = nullptr;
                break;
            }
        }

        return head;
    }
};