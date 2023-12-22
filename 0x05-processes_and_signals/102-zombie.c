#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates zombie processes using fork().
 *
 * Return: Always returns EXIT_SUCCESS.
 */
int main(void)
{
	pid_t pp;
	char c = 0;

	while (c < 5)
	{
		pp = fork();
		if (pp > 0)
		{
			printf("Zombie process created, PID: %d\n", pp);
			sleep(1);
			c++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
