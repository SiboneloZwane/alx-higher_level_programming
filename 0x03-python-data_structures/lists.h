#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @n: int
 * @next: points to the next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
int _strlen_recursion(char *s);
int check_palin(char *s, int start, int end);
int is_palin(char *s);
#endif /* LISTS_H */
