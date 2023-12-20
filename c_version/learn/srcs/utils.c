#include "linear.h"

int create_output_file(char *name)
{
	return (open(name, O_CREAT | O_WRONLY));
}

int open_input_file(char *name)
{
	return (open(name, O_RDONLY));
}

int ft_error(int type, char **argv, t_theta *theta, t_data *data)
{
	switch (type)
	{
		case (E_ARG):
			printf("Usage: %s <output csv_file>\n", argv[0]);
			break;
		case (E_OPEN):
			printf("Error open file.\n");
			break;
		case (E_MALLOC):
			printf("Error malloc.\n");
		default:
			printf("error\n");
			break;
	}
	ft_lstclear(data);
	free(theta);
	return (1);
}

int ft_lstsize(t_data *data)
{
	int	i;

	i = 0;
	while (data)
	{
		i++;
		data = data->next;
	}
	return (i);
}

void ft_lstclear(t_data *data)
{
	t_data	*next;
	while (data)
	{
		next = data->next;
		free(data);
		data = next;
	}
}
