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
        std::stack<int> stack;
        ListNode* cur = head;

        // Traverse the list and push each node's value onto the stack
        while (cur) {
            stack.push(cur->val);
            cur = cur->next;
        }

        // Traverse the list again and compare each node's value with the stack's top
        cur = head;
        while (cur && cur->val == stack.top()) {
            stack.pop();
            cur = cur->next;
        }

        // If the list is a palindrome, cur should be null after the comparison
        return !cur;
        
    }
};