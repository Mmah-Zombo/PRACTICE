#include <stdio.h>
#include <stdlib.h>


typedef struct stack_t
{
    /* data */
    int n;
    int *prev;
    int *next;
}stack_t;

stack_t *top;

void push (int n)
{
    stack_t *newNode;
    newNode = malloc(sizeof(stack_t));

    if (newNode == NULL)
    {
        exit(1);
    }

    newNode->n = n;
    newNode->prev = NULL;


    newNode->next = top;
    top->prev = newNode;
    top = newNode;  
}

int pop()
{
    stack_t *tmp;
    tmp = top;
    

    int value;
    if (top == NULL)
    {
        exit(1);
    }

    return (value);
}
int main (void)
{

    return (0);
}