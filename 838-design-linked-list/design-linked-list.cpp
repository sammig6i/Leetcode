class Node {
public:
    int val;
    Node* next;

    Node() {}
    Node(int val) : val(val), next(nullptr) {}
};

class MyLinkedList {
public:
    Node* head  = new Node();
    int len = 0;

    MyLinkedList() {}

    int get(int index) {
        if (len == 0) {
            return -1;
        }

        Node* cur = head;
        while (cur && index > 0) {
            cur = cur->next;
            --index;
        }

        if (!cur) {
            return -1;
        }

        return cur->val;
    }

    void addAtHead(int val) {
        Node* node = new Node(val);
        if (len == 0) {
            head = node;
        } else {
            node->next = head;
            head = node;
        }
        ++len;
    }

    void addAtTail(int val) {
        Node* node = new Node(val);
        if (len == 0) {
            head = node;
        } else {
            Node* cur = head;
            while (cur->next) {
                cur = cur->next;
            }
            cur->next = node;
        }
        ++len;
    }

    void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
        } else if (index == len) {
            addAtTail(val);
        } else if (index < len) {
            Node* node = new Node(val);
            
            Node* cur = head;
            while (cur && index > 1) {
                cur = cur->next;
                --index;
            }

            node->next = cur->next;
            cur->next = node;
            ++len;
        }
    }

    void deleteAtIndex(int index) {
        if (index < len) {
            if (index == 0) {
                head = head->next;
            } else {
                Node* cur = head;
                while (cur->next && index > 1) {
                    cur = cur->next;
                    --index;
                }
                cur->next = cur->next->next;
            }
            --len;
        }
       
        
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