#include<stdio.h>
#include "solve.c"

void main()
{
    xor_list* list = malloc(sizeof(xor_list));
    list->element = 12;
    list->address = 0;

    add(list, 15);
    add(list, 3);
    add(list, 4);
    add(list, 12);
    add(list, 9);

    printf("%d\n", get(list, 0));
    printf("%d\n", get(list, 1));
    printf("%d\n", get(list, 2));
    printf("%d\n", get(list, 3));
    printf("%d\n", get(list, 4));
    printf("%d\n", get(list, 5));
}
