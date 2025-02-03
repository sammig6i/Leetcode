class MyLinkedList {
private:
    struct ListNode {
        int val;
        ListNode *next;
        ListNode *prev;
        ListNode() : val(0), prev(nullptr), next(nullptr) {}
        ListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
        ListNode(int x, ListNode *next, ListNode *prev) : val(x), prev(nullptr), next(nullptr) {}
    };

    ListNode* head;
    ListNode* tail;
    int size;

public:
    MyLinkedList() {
        head = new ListNode(-1);
        tail = new ListNode(-1);
        head->next = tail;
        tail->prev = head;
        size = 0;
    }
    
    int get(int index) {
        ListNode *cur = head->next;
        int i = 0;
        while (cur && cur != tail) {
            if (i == index) {
                return cur->val;
            }
            cur = cur->next;
            ++i;
        }
        return -1;
    }
    
    void addAtHead(int val) {
        ListNode* new_node = new ListNode(val), *next_node = head->next;
        new_node->next = next_node;
        new_node->prev = head;
        head->next = new_node;
        next_node->prev = new_node;
        ++size;
    }
    
    void addAtTail(int val) {
        ListNode* new_node = new ListNode(val), *prev_node = tail->prev;
        new_node->next = tail;
        new_node->prev = prev_node;
        prev_node->next = new_node;
        tail->prev = new_node;
        ++size;
    }
    
    void addAtIndex(int index, int val) {
        ListNode* new_node = new ListNode(val);
        ListNode* prev_node = head, *cur = head->next;
        int i = 0;
        if (index == 0) {
            addAtHead(val);
            return;
        }

        if (index == size) {
            addAtTail(val);
            return;
        }

        while (cur) {
            if (i == index) {
                new_node->next = cur;
                new_node->prev = prev_node;
                prev_node->next = new_node;
                cur->prev = new_node;
                ++size;
                return;
            }
            prev_node = cur;
            cur = cur->next;
            ++i;
        }
        return;
    }
    
    void deleteAtIndex(int index) {
        ListNode* cur = head->next, *prev_node = head;
        int i = 0;
        while (cur != tail) {
            if (i == index) {
                ListNode* next_node = cur->next;
                prev_node->next = next_node;
                next_node->prev = prev_node;
                --size;
                return;
            }
            prev_node = cur;
            cur = cur->next;
            ++i;
        }

        return;
        
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */