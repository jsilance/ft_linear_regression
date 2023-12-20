#ifndef LINEAR_H
# define LINEAR_H

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <fcntl.h>
# include <math.h>
# include <unistd.h>
# include "get_next_line.h"

enum e_errors
{
	E_ARG = 1,
	E_OPEN,
	E_MALLOC
};

typedef struct s_theta
{
	double	p;
	double	m;
}	t_theta;

typedef struct s_data
{
	double			km;
	double			price;
	struct s_data	*next;
}	t_data;

int		ft_error(int type, char **argv, t_theta *theta, t_data *data);
int		create_output_file(char *name);
int		open_input_file(char *name);
int		ft_lstsize(t_data *data);
void	ft_lstclear(t_data *data);
void	ft_lstadd_back(t_data **data, t_data *new);
t_data	*init_data(int fd);

double	estimate_prive(double mileage, t_theta *theta);
double	sum_estimate_a(t_data *datas, t_theta *theta);
double	sum_estimate_b(t_data *datas, t_theta *theta);
void	update_theta(t_theta *theta, t_data *data, double learning_rate);
double	descent_grad(t_theta *theta, t_data *datas);

#endif
