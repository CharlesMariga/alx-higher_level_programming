#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * is_palindrome - Linked list palindrome
 *
 * @head: head of the linked list
 *
 * Description: checks if a linked list is a palindrom
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed_list;
	listint_t *current;
	listint_t *new_node;
	listint_t *new_prev_node;
	int counter = 0;

	if (*head == NULL)
		return (1);

	new_prev_node = NULL;
	current = *head;
	while (current != NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (0);

		if (counter == 0) {
			new_node->n = current->n;
			new_node->next = NULL;
		} else {
			new_node->n = current->n;
			new_node->next = new_prev_node;
		}
		new_prev_node = new_node;
		current = current->next;
		counter++;
	}
	reversed_list = new_prev_node;

	current = *head;
	while (current != NULL)
	{
		if (current->n != reversed_list->n)
		{
			free(new_node);
			return (0);
		}
		current = current->next;
		reversed_list = reversed_list->next;
	}
	free(reversed_list);

	return (1);
}
