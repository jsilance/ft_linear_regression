#include "linear.h"

double estimate_prive(double mileage, t_theta *theta)
{
	return (theta->p + theta->m * mileage);
}

double sum_estimate_a(t_data *datas, t_theta *theta)
{
	double	sum_value;
	t_data	*data;

	sum_value = 0;
	data = datas;
	while (data)
	{
		sum_value += (estimate_prive(data->km, theta) - data->price) / data->km;
		data = data->next;
	}
	return (sum_value);
}

double sum_estimate_b(t_data *datas, t_theta *theta)
{
	double	sum_value;
	t_data	*data;

	sum_value = 0;
	data = datas;
	while (data)
	{
		sum_value += (estimate_prive(data->km, theta) - data->price);
		data = data->next;
	}
	return (sum_value);
}

void update_theta(t_theta *theta, t_data *data, double learning_rate)
{
	double	elems;

	elems = ft_lstsize(data);

	theta->p -= learning_rate * (double)(1.0 / elems) * sum_estimate_b(data, theta);
	theta->m += learning_rate * (double)(1.0 / elems) * sum_estimate_a(data, theta);
}

double descent_grad(t_theta *theta, t_data *datas)
{
	double	j;
	double	elems;
	t_data	*data;

	data = datas;
	j = 0;
	elems = ft_lstsize(data);
	while (data)
	{
		j += pow((estimate_prive(data->km, theta) - data->price), 2.0);
		data = data->next;
	}
	j = ((double)1.0 / ((double)2.0 * elems)) * j;
	return (j);
}