#include "linear.h"

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


	fd_out = create_output_file("learned_data.csv");
	if (fd_out == -1)
		return (ft_error(E_OPEN, NULL, NULL, NULL));

	theta = init_theta();
	if (!theta)
		return (ft_error(E_MALLOC, NULL, theta, data));

	fd_in = open_input_file(argv[1]);
	if (fd_in == -1)
		return (ft_error(E_OPEN, NULL, NULL, NULL));
	
	// data = init_data(fd_in);
	// close(fd_in);
	// close(fd_out);
	return (0);
}
