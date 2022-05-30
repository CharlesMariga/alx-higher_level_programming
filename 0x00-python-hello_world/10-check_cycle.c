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
	listint_t *current, *checker;
	int i = 0, j = 0;

	current = list;
	while (current != NULL)
	{
		j = 0;
		checker = list;
		while (i < j)
		{
			if (i != j && current == checker)
			{
				return (1);
			}
			checker = checker->next;
			j++;
		}
		current = current->next;
		i++;
	}

	return (0);
}
