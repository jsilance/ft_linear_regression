import sys
import csv

def estimate_price(mileage, theta):
	return theta[0] + theta[1] * mileage

def main():
	if len(sys.argv) != 3:
		print("Usage: python3 {} <csv_file>".format(sys.argv[0]), "<value to estimate>")
		sys.exit(1)

	csv_file = sys.argv[1]
	value = int(sys.argv[2])
	theta = []
	try:
		with open(csv_file, 'r') as f:
			reader = csv.reader(f)
			next(reader)
			for row in reader:
				theta = [float(row[0]), float(row[1]), float(row[2])]
				break
		print("Estimated price:", estimate_price(value, theta))
		print("Coef corelation:", theta[2])
	except Exception as e:
		print("Error:", e)
		sys.exit(1)

if __name__ == "__main__":
	main()