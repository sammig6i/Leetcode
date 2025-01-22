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
        if (left == 1) {
            return reverseList(head, right).first;
        }
        head->next = reverseBetween(head->next, left - 1, right - 1);
        return head;
    }
    
private:
    pair<ListNode*, ListNode*> reverseList(ListNode* node, int n) {
        if (n == 1) {
            return {node, node->next};
        }
        auto res = reverseList(node->next, n - 1);
        node->next->next = node;
        node->next = res.second;
        return {res.first, res.second};
    }

};



