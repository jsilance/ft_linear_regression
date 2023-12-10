# # from matplotlib import pyplot as plt
import csv

def estimate_price(mileage, theta):
	return theta[0] + theta[1] * mileage

def sumEstimateA(data, theta):
	sum = 0
	for x, y in data:
		sum += (estimate_price(x, theta) - y) * x
	return sum

def sumEstimateB(data, theta):
	sum = 0
	for x, y in data:
		sum += estimate_price(x, theta) - y
	return sum

def update_theta(theta, data, learning_rate):
	tmp_theta = [0, 0]
	m = len(data)
	for x, y in data:
		tmp_theta[0] += (estimate_price(x, theta) - y)
		tmp_theta[1] += (estimate_price(x, theta) - y) * x
	# tmp_theta[0] = theta[0] - learning_rate * (1 / m) * sumEstimateB(data, theta)
	# tmp_theta[0] = learning_rate * (1 / m) * sumEstimateB(data, theta)
	# tmp_theta[1] = theta[1] - learning_rate * (1 / m) * sumEstimateA(data, theta)
	# tmp_theta[1] = learning_rate * (1 / m) * sumEstimateA(data, theta)
	tmp_theta[0] *= (1 / m)
	tmp_theta[1] *= (1 / m)

	theta[0] -= learning_rate * tmp_theta[0]
	theta[1] -= learning_rate * tmp_theta[1]
	return theta

with open('data.csv', 'r') as file:
	reader = csv.reader(file)
	next(reader)
	data = list(reader)
	data = [(float(el[0]), float(el[1])) for el in data]
	theta = [0, 0]
	learning_rate = 0.00001
	for _ in range(500):
		theta = update_theta(theta, data, learning_rate)
	print("Theta B: ", theta[0])
	print("Theta A: ", theta[1])
