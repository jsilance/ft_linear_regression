import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import csv

# ------ Gradient descent ---------------

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
# ---------------------------------------

# ------ Graphic functions --------------

def point_init_plt(data, theta):
	plt.clf()
	line_y = []
	line_x = [x for x, y in data]
	for x, y in data:
		plt.scatter(x, y, color='red')
		line_y.append((theta[0] + theta[1] * x))
	plt.plot(line_x, line_y)
	plt.ylabel('Prix')
	plt.xlabel('Km')
	plt.draw()

def drawlines_plt(data, theta):
	line_y = []
	line_x = [x for x, y in data]
	for x, y in data:
		line_y.append((theta[0] + theta[1] * x))
	plt.plot(line_x, line_y)
	plt.draw()
# ---------------------------------------

# ------ Calcul coef corelation ---------

def covariance(data):
	x = [x for x, y in data]
	y = [y for x, y in data]
	moy_xy = 0
	for dx, dy in data:
		moy_xy += dx * dy
	moy_xy /= len(data)
	
	moy_x = 0
	for val in x:
		moy_x += val
	moy_x /= len(x)

	moy_y = 0
	for val in y:
		moy_y += val
	moy_y /= len(y)
	return (moy_xy - (moy_x * moy_y))

def variance(data, val):
	x = [x for x, y in data]
	y = [y for x, y in data]
	if (val == 0):
		return (np.var(x))
	return (np.var(y))

def coefCorelation(data):
	if (math.sqrt(variance(data, 0)) == 0):
		return (-2)
	if (math.sqrt(variance(data, 1)) == 0):
		return (-2)

	coef = covariance(data) / (math.sqrt(variance(data, 0)) * math.sqrt(variance(data, 1)))
	return (coef)
# ---------------------------------------

# ------ Write to file ------------------

def writeOutputData(theta, corelation):
	with open("learned_data.csv", 'w') as file:
		writer = csv.writer(file)
		writer.writerow(['theta0', 'theta1', 'corelation'])
		writer.writerow([theta[0], theta[1], corelation])
# ---------------------------------------

# ------ Options d'apprentissage --------

graphic_mode = 1 # 0 no graphic, 1 basic graphic (slow), 2 graphich with history (very slow)
learning_rate = 1.0
num_iterations = 20000000
stabilisation = 1.0 * 10 ** -15
# ---------------------------------------

data = list()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 {} <output csv_file>".format(sys.argv[0]))
		exit(1)
	try:
		with open(sys.argv[1], 'r') as file:
			reader = csv.reader(file)
			next(reader)
			data = list(reader)
			data = [(float(el[0]), float(el[1])) for el in data]
	except Exception as e:
		print("Error:", e)
		exit(1)

	theta = [0, 0]
	cost = 1
	# ---------------------------------------

	if (graphic_mode >= 1):
		plt.ion()
		point_init_plt(data, [0, 0])

	# ------ Iteration epoch ----------------
	for _ in range(num_iterations):
		old_cost = cost
		theta = update_theta(theta, data, learning_rate)
		cost = descent_grad(theta, data)
		
		# ------ graphic part ---------------
		if (graphic_mode == 1):
			point_init_plt(data, theta)
		if (graphic_mode >= 1):
			drawlines_plt(data, theta)
			plt.pause(0.1)
		# -----------------------------------

		if (old_cost == 0):
			break
		if (abs(abs(cost / old_cost) - 1) < stabilisation):
			break
	# ---------------------------------------

	if (graphic_mode >= 1):
		plt.ioff()
		print("Learning complete.")
		plt.show()

	coefCore = coefCorelation(data)

	if (old_cost):
		print("Learning complete with: " + str(100 - abs(100 - abs(cost / old_cost) * 100)) + "% of stabilisation.")
	if (coefCore == -2):
		print("Constant detected!")
	else:
		print("Corelation coeficient: ", coefCore)

	print("\nReady to estimate the price.")


	writeOutputData(theta, coefCore)

if __name__ == "__main__":
	main()