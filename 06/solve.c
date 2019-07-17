#include<stdlib.h>

typedef struct xor_list {
    int element;
    unsigned int address;
} xor_list;

xor_list* getLastElement(xor_list* l)
{
    // Only has one element
    if (l->address == 0) {
        return l;
    }

    // Has multiple elements
    xor_list* prev_puppet = l;
    xor_list* puppet = prev_puppet->address;
    
    unsigned int next_address;
    while (puppet->address != prev_puppet) {
        next_address = puppet->address ^ (unsigned int)prev_puppet;
        prev_puppet = puppet;
        puppet = next_address;    
    }

    return puppet;
}

void add(xor_list* l, int element) 
{    
    xor_list* puppet = getLastElement(l);
    xor_list* new_node = malloc(sizeof(xor_list));
 
    new_node->element = element;
    new_node->address = puppet;
    puppet->address = puppet->address ^ (unsigned int)new_node;
}

int get(xor_list* l, int index) 
{
    xor_list* puppet = l;
    unsigned int current_address, prev_address = 0;

    while (index > 0) {
        current_address = puppet;
        puppet = puppet->address ^ prev_address;
        prev_address = current_address;
        index --;
    }

    return puppet->element;
}

