import csv

def estimate_price(mileage, theta):
	return theta[0] + theta[1] * mileage

def sumEstimateA(data, theta):
	sum_value = 0
	for x, y in data:
		sum_value += (estimate_price(x, theta) - y) / x
	return sum_value

def sumEstimateB(data, theta):
	sum_value = 0
	for x, y in data:
		sum_value += (estimate_price(x, theta) - y)
	return sum_value

def update_theta(theta, data, learning_rate):
	m = len(data)

	theta[0] -= learning_rate * (1 / m) * sumEstimateB(data, theta)
	theta[1] += learning_rate * (1 / m) * sumEstimateA(data, theta)

	return theta

def descent_grad(theta, data):
	J = 0
	m = len(data)
	for x, y in data:
		J += (estimate_price(x, theta) - y) ** 2
	J = (1 / (2 * m)) * J
	return J

with open('generated_data.csv', 'r') as file:
	reader = csv.reader(file)
	next(reader)
	data = list(reader)
	data = [(float(el[0]), float(el[1])) for el in data]
	theta = [0, 0]
	learning_rate = 0.50
	num_iterations = 240000
	cost = 1
	for _ in range(num_iterations):
		old_cost = cost
		theta = update_theta(theta, data, learning_rate)
		cost = descent_grad(theta, data)
		# if ((abs(cost - old_cost)) / old_cost < 0.0001 ):
		# 	break
		print("Theta B:", theta[0])
	print("Theta B:", theta[0])
	print("Theta A:", theta[1])
	print("Cost:", cost)
