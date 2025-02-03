class Node {
public:
    int data;
    Node *next;

    Node () {

    }

    Node(int val) {
        data=val;
        next=NULL;
    }

};

class MyLinkedList {
public:

    Node *head = new Node();
    int len=0;

    MyLinkedList() {
        
    }
    
    int get(int index) {
        if(len==0) {
            return -1;
        }

        Node *temp=head;

        while(temp!=NULL && index>0) {
            temp=temp->next;
            index--;
        }

        if(temp==NULL) {
            return -1;
        }

        return temp->data;
    }
    
    void addAtHead(int val) {

        Node *node = new Node(val);

        if(len==0) {
            head = node;
        } else {
            node->next=head;
            head=node;
        }
        len++;
        
    }
    
    void addAtTail(int val) {
        Node *node = new Node(val);

        if(len==0) {
            head=node;
        } else {
            Node *temp = head;

            while (temp->next!=NULL) {
                temp=temp->next;
            }

            temp->next=node;
        }

        len++;
    }
    
    void addAtIndex(int index, int val) {
        Node *node = new Node(val);

        if(index==0) {
            addAtHead(val);
        } else if(index==len) {
            addAtTail(val);
        } else if(index<len) {
            Node *temp = head;
            while(temp->next!=NULL && index>1) {
                temp=temp->next;
                index--;
            }
            node->next=temp->next;
            temp->next=node;
            len++;
        }


    }
    
    void deleteAtIndex(int index) {
        if(index<len) {
            Node *temp=head;

            if(index==0) {
                head=head->next;
            } else {
                while(temp->next!=NULL && index>1) {
                    temp=temp->next;
                    index--;
                }

                temp->next=temp->next->next;
                len--;
            }

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