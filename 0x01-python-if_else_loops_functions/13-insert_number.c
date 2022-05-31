#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a node
 *
 * @head: head of the linked list
 * @number: number to be inserted in the linked list
 *
 * Description: inserts number into a linked list in a sorted order
 *
 * Return: sorted linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;
	listint_t *prev;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	prev = NULL;
	current = *head;
	while (current && current->next != NULL)
	{
		if (current->n > number)
			break;
		prev = current;
		current = current->next;
	}

	if (head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
	} else if (prev) {
		new_node->next = current;
		prev->next = new_node;
	} else {
		new_node->next = current;
	}

	return (new_node);
}
