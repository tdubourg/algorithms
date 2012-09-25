/***
Author: TD
License: GPLv3
***/

struct node {
    int data;
    struct node *next;
};

struct node *reverse(struct node *node) {
    if(NULL == node)
        return node;
    
    node* prev = NULL;
    node* tmp = NULL;
    while(NULL != node) {
        tmp = node->next;
        node->next = prev;
        prev = node;
        node = tmp;
    }
    return prev;
}
