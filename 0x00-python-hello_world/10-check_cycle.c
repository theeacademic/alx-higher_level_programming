/**
 * main - Example usage to test the check_cycle function
 *
 * Return: Always 0
 */
int main(void)
{
   
    listint_t *node1 = malloc(sizeof(listint_t));
    listint_t *node2 = malloc(sizeof(listint_t));
    listint_t *node3 = malloc(sizeof(listint_t));

    int hasCycle;

    node1->data = 1;
    node1->next = node2;

    node2->data = 2;
    node2->next = node3;

    node3->data = 3;
    node3->next = node1;

    hasCycle = check_cycle(node1);

    if (hasCycle)
    {
        printf("The linked list has a cycle.\n");
    }
    else
    {
        printf("The linked list does not have a cycle.\n");
    }
    free(node1);
    free(node2);
    free(node3);

    return 0;
}
