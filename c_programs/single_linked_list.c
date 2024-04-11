#include <stdio.h>
#include <stdlib.h>

/*The node for the linked list*/
struct node
{
    int data;
    struct node *link;
};

/*This prints the value in each node of a linked list*/
void print_node_data(struct node *hd)
{
    if (hd == NULL)
    {
        printf("This is an empty list!\n");
    }
    else
    {
        struct node *ptr;
        ptr = hd;
        while (ptr != NULL)
        {
            printf("%d ", ptr->data);

            /**This causes the ptr pointer to point to
             * the address in its link container
            */
            ptr = ptr->link;
        }
        printf("\n");
    }
}


int main(void)
{
    /**A pointer to keep track of our first node is created
     * and is made to hold the address of a newly created node
     * i.e the first node
    */
    struct node *head = malloc(sizeof(struct node));

    /*A pointer to go through the linked list*/
    struct node *current;
    current = head; 

    int i;
    int numbers[5] = {23, 50, 60, 4, 7};

    /**The nodes are created and assigned the corresponding
     * values of the array of integers above
    */
    for (i = 0; i < 5; i++)
    {
        current->data = numbers[i];
        if (i != 4)
        {
            current->link = malloc(sizeof(struct node));
            current = current->link;
        }
        else
        {
            current->link = NULL;
        }
    }

    print_node_data(head);
    return 0;
}
