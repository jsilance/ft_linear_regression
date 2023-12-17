import matplotlib.pyplot as plt
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


# ------ Graphic functions --------------

def point_init_plt(data, theta):
	plt.clf()
	line_y = []
	line_x = []
	for x, y in data:
		plt.scatter(x, y, color='red')
		line_y.append((theta[0] + theta[1] * x))
		line_x.append(x)
	plt.plot(line_x, line_y)
	plt.ylabel('Prix')
	plt.xlabel('Km')
	plt.draw()

def drawlines_plt(data, theta):
	line_y = []
	line_x = []
	for x, y in data:
		line_y.append((theta[0] + theta[1] * x))
		line_x.append(x)
	plt.plot(line_x, line_y)
	plt.draw()
# ---------------------------------------

data = list()

with open('data.csv', 'r') as file:
	reader = csv.reader(file)
	next(reader)
	data = list(reader)
	data = [(float(el[0]), float(el[1])) for el in data]

theta = [0, 0]
cost = 1

# ------ Options d'apprentissage --------

graphic_mode = 2 # 0 no graphic, 1 basic graphic (slow), 2 graphich with history (very slow)
learning_rate = 0.7
num_iterations = 2000000000
precision = 0.00000000000000000001
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
		plt.pause(0.05)
	# print(abs(cost / old_cost) - 1)
	# -----------------------------------

	if (abs(abs(cost / old_cost) - 1) < precision):
		break
# ---------------------------------------

if (graphic_mode >= 1):
	plt.ioff()
	# plt.show()

print("Learning complete with: " + str(100 - abs(100 - abs(cost / old_cost) * 100)) + "% of precision.")
print("Ready to estimate the price.")