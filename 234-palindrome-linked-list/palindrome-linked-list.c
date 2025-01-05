/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int isPalindrome(struct ListNode* head) {
    if (head == NULL) return 1;  // An empty list is a palindrome

    // Stack to store values from the list
    int size = 0;
    struct ListNode* cur = head;
    while (cur != NULL) {
        size++;
        cur = cur->next;
    }

    // Step 2: Dynamically allocate memory for the stack
    int* stack = (int*)malloc(size * sizeof(int));
    if (stack == NULL) {
        perror("Failed to allocate memory for stack");
        exit(EXIT_FAILURE);
    }

    int top = -1;
    cur = head;
    while (cur != NULL) {
        stack[++top] = cur->val;
        cur = cur->next;
    }

    // Traverse the list again and compare the values with the stack
    cur = head;
    while (cur != NULL) {
        if (cur->val != stack[top--]) {
            return 0;  // Not a palindrome
        }
        cur = cur->next;
    }

    return 1;  // It's a palindrome
}