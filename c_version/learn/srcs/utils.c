#include "linear.h"

int create_output_file(char *name)
{
	unlink(name);
	return (open(name, O_CREAT | O_WRONLY, 777));
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
			printf("Error cannot open file.\n");
			break;
		case (E_MALLOC):
			printf("Error malloc.\n");
			break;

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

void ft_lstadd_back(t_data **data, t_data *new)
{
	t_data	*last;

	if (!*data)
	{
		*data = new;
		return ;
	}
	last = *data;
	while (last->next)
		last = last->next;
	last->next = new;
}

t_data *init_data(int fd)
{
	t_data	*data;
	t_data	*new;
	char	*line;

	data = NULL;
	line = NULL;
	line = get_next_line(fd);
	free(line);
	line = get_next_line(fd);
	while (line)
	{
		new = (t_data *)malloc(sizeof(t_data));
		if (!new)
		{
			ft_lstclear(data);
			return (NULL);
		}
		new->next = NULL;
		new->km = atoi(line);
		new->price = atoi(strchr(line, ',') + 1);
		ft_lstadd_back(&data, new);
		free(line);
		line = get_next_line(fd);
	}
	return (data);
}