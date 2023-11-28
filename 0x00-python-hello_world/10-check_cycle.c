#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast; /* two traversals through the list */

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;  /* move through the list 1 step at a time*/
		fast = fast->next->next; /* move throughthe list 2 steps at a time*/

		/* if the pointers meet at any point, there is a cycle, return 1 */
		if (slow == fast)
			return (1);

	}

	/* if there is no cycle, return 0 */
	return (0);
}
