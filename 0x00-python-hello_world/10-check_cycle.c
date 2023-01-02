#include "lists.h"

/**
 * check_cycle - cheks if a linked list has a cycle
 * @list: the linked list to check
 *
 * Return: 0 if no cycle and 1 if a cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *prev;

	temp = list;
	prev = list;
	while (list && temp && temp->next)
	{
		list = list->next;
		temp = temp->next->next;

		if (list == temp)
		{
			list = prev;
			prev =  temp;
			while (1)
			{
				temp = prev;
				while (temp->next != list && temp->next != prev)
					temp = temp->next;

				if (temp->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
