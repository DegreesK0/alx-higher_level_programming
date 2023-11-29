#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the pointer of the head of the linked list
 * @number: number to be inserted into the linked list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	/* assign memory to new_node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL) /* check that malloc worked successfully */
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	prev = NULL; /* variable to find position in list */

	/* while the current number is not NULL and is less than number keep moving */
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	/* if the previous was NULL, means we remain at the head position*/
	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	/* Otherwise, use the previous data to create a new_node */
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
