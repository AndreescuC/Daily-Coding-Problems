#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "solve.c"

typedef struct Test{
    int* array;
    int size;
    int result;
} Test;

Test* getTests(int *no_tests)
{
    *no_tests = 2;
    Test *tests = malloc(*no_tests * sizeof(Test));

    Test t1;
    t1.size = 4;
    t1.result = 2;
    int test1[4] = {3, 4, -1, 1};
    t1.array = malloc(t1.size * sizeof(int));
    memcpy(t1.array, test1, sizeof(test1));
    tests[0] = t1;
    
    Test t2;
    t2.size = 3;
    t2.result = 3;
    int test2[3] = {1, 2, 0};
    t2.array = malloc(t2.size * sizeof(int));
    memcpy(t2.array, test2, sizeof(test2));
    tests[1] = t2;

    return tests;
}

void main()
{
    int i, n, result;
    Test *tests = getTests(&n);

    for (i = 0; i < n; i++) {
        printf("Test %d: ", i);
        result = getMissing(tests[i].array, tests[i].size);
        if (result != tests[i].result) {
            printf("fail! Expected %d, given %d\n\n", tests[i].result, result);
        } else {
            printf("passed!\n\n");
        }
    }
}

