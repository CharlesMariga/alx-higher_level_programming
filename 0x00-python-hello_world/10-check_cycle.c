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
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		if (list == current->next)
		{
			return (1);
		}

		current = current->next;
	}

	return (0);
}
