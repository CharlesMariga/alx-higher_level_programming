#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

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
	listint_t *prev;
	listint_t *current;
	listint_t *temp;

	if (*head == NULL)
		return (1);

	reversed_list = malloc(sizeof(listint_t));
	if (reversed_list == NULL)
		return (0);

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
		}
	reversed_list = prev;

	current = reversed_list;
	while (current != NULL)
	{
		if (current->n != reversed_list->n)
		{
			free(reversed_list);
			return (0);
		}
		current = current->next;
		reversed_list = reversed_list->next;
	}
	free(reversed_list);

	return (1);
}
