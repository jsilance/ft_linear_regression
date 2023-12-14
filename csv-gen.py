import csv
import random

def generate_data(num_samples=10000):
	data = []
	for _ in range(num_samples):
		km = random.uniform(5000, 200000)
		price = 15000 - (km / 1000) + random.uniform(-500, 500)
		data.append([km, price])
	return data

def save_to_csv(data, filename='generated_data.csv'):
	with open(filename, 'w') as file:
		writer = csv.writer(file)
		writer.writerow(['km', 'price'])
		writer.writerows(data)

generated_data = generate_data()
save_to_csv(generated_data, 'generated_data.csv')