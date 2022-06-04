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
	listint_t *current;
	int counter = 0;
	int *p;
	int i;

	current = *head;
	while (current != NULL)
	{
		counter++;
		current = current->next;
	}

	p = malloc(sizeof(int) * counter);
	if (p == NULL)
		return (0);

	current = *head;
	i = 0;
	while (current != NULL)
	{
		*(p + counter - 1 - i) = current->n;
		current = current->next;
		i++;
	}

	i = 0;
	current = *head;
	while (i < counter)
	{
		if (current->n != *(p + i))
		{
			free(p);
			return (0);
		}
		current = current->next;
		i++;
	}

	return (1);
}
