#include "linear.h"

const int g_iter = 2000000000;
double g_learning_rate = 0.1;
double g_precision = 0.0000000000001;

static t_theta *init_theta(void)
{
	t_theta	*theta;

	theta = (t_theta *)malloc(sizeof(t_theta));
	if (!theta)
		return (NULL);
	theta->m = 0;
	theta->p = 0;
	return (theta);
}

void print_data(t_data *data)
{
	while (data)
	{
		printf("km: %f, price: %f\n", data->km, data->price);
		data = data->next;
	}
}

void write_to_csv(t_theta *theta, int fd)
{
	write(fd, "theta0,theta1,corelation\n", 25);
	dprintf(fd, "%f,%f,%f\n", theta->p, theta->m, 0.0);
}

void epoch(t_theta *theta, t_data *data, double learning_rate)
{
	int		i;
	double	cost;
	double	prev_cost;

	i = 0;
	cost = 1;
	while (i < g_iter)
	{
		prev_cost = cost;

		update_theta(theta, data, learning_rate);
		// printf("theta0: %f, theta1: %f\n", theta->p, theta->m);
		cost = descent_grad(theta, data);
		if (prev_cost == 0 || fabs(fabs(cost / prev_cost) - 1) < g_precision)
			break;
		i++;
	}
}

int main(int argc, char **argv)
{
	int		fd_in;
	int		fd_out;
	t_theta *theta;
	t_data	*data;

	fd_in = -1;
	fd_out = 0;
	if (argc != 2)
		return (ft_error(E_ARG, argv, NULL, NULL));
	theta = init_theta();
	if (!theta)
		return (ft_error(E_MALLOC, NULL, theta, NULL));
	fd_in = open_input_file(argv[1]);
	if (fd_in == -1)
		return (ft_error(E_OPEN, NULL, NULL, NULL));

	fd_out = create_output_file("learned_data.csv");
	if (fd_out == -1)
	{
		close(fd_in);
		return (ft_error(E_OPEN, NULL, NULL, NULL));
	}

	
	data = init_data(fd_in);

	epoch(theta, data, g_learning_rate);

	write_to_csv(theta, fd_out);

	free(theta);
	ft_lstclear(data);
	close(fd_in);
	close(fd_out);
	printf("Learning finished.\n");
	return (0);
}
