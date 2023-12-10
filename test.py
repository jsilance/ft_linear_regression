# Fonction de coût (exemple : une fonction quadratique)
def cost_function(theta, points):
    total_cost = 0
    for x, y in points:
        total_cost += (theta[0] + theta[1] * x - y)**2
    return total_cost / (2 * len(points))

# Dérivées partielles de la fonction de coût
def gradient(theta, points):
    d_theta0 = 0
    d_theta1 = 0
    m = len(points)

    for x, y in points:
        d_theta0 += (theta[0] + theta[1] * x - y)
        d_theta1 += (theta[0] + theta[1] * x - y) * x

    d_theta0 /= m
    d_theta1 /= m

    return [d_theta0, d_theta1]

# Algorithme de descente de gradient
def gradient_descent(initial_theta, learning_rate, num_iterations, points):
    theta = initial_theta.copy()

    for _ in range(num_iterations):
        gradient_value = gradient(theta, points)
        theta[0] -= learning_rate * gradient_value[0]
        theta[1] -= learning_rate * gradient_value[1]

    return theta

# Points dans le plan en 2D (exemples)
data_points = [(240000, 3650),(139800, 3800),(150500, 4400),(185530, 4450),(176000, 5250),(114800, 5350),(166800, 5800),(89000, 5990),(144500, 5999),(84000, 6200),(82029, 6390),(63060, 6390),(74000, 6600),(97500, 6800),(67000, 6800),(76025, 6900),(48235, 6900),(93000, 6990),(60949, 7490),(65674, 7555),(54000, 7990),(68500, 7990),(22899, 7990),(61789, 8290)]

# Paramètres initiaux
initial_theta = [0.0, 0.0]

# Taux d'apprentissage
learning_rate = 0.1

# Nombre d'itérations
num_iterations = 100

# Exécution de la descente de gradient
optimized_theta = gradient_descent(initial_theta, learning_rate, num_iterations, data_points)

print("Paramètres optimisés:", optimized_theta)
print("Valeur de la fonction de coût minimisée:", cost_function(optimized_theta, data_points))
