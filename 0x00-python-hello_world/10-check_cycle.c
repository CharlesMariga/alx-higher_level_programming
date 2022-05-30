#include "lists.h"

/**
 * check_cycle - checks whether a singly linked list has a
 * cycle in it
 *
 * @list: singly linked list to be checked
 *
 * Description: checks whether a singly linked list **list** has cycle in it
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prev;
	listint_t *current;

	prev = list;
	current = list;
	while (current)
	{
		if (current->next == NULL)
			return (0);
		prev = prev->next;
		current = current->next->next;

		if (prev == current)
		{
			return (1);
		}
	}

	return (0);
}
