import matplotlib.pyplot as plt 
import numpy as np 


def plot_reference_points(x_values, y_values):
	print(len(x_values), len(y_values))

	updated_x = []
	updated_y = []

	for i in range(len(x_values)):

		if i % 10 == 0:
			updated_x.append(x_values[i])
			updated_y.append(y_values[i])

	#print(plot_data)
	plt.scatter(updated_x, updated_y)
	plt.show()

	return 

def read_points():

	file_name = "ref_points_1.txt"
	x_values = []
	y_values = []

	with open(file_name, "r") as rfile:

		lines = rfile.readlines()
		for each_line in lines:
			# print(each_line)

			if "x" in each_line:
				each_line = each_line.strip()
				each_line = each_line.split(":")
				x_values.append(float(each_line[1]))

			if "y" in each_line:
				each_line = each_line.strip()
				each_line = each_line.split(":")
				y_values.append(float(each_line[1]))

	print(x_values)
	print(y_values)

	plot_data = []

	for i in range(len(x_values)):

		each_x = x_values[i]
		each_y = y_values[i]

		plot_data.append([each_x, each_y])

	return x_values, y_values


def order_points(x_values, y_values):

	control_points = []

	for i in range(0, len(x_values)):
		control_points.append((x_values[i], y_values[i]))

	return control_points


def sample_points(x_values, y_values):

	updated_x = []
	updated_y = []

	for i in range(len(x_values)):

		if i % 10 == 0:
			updated_x.append(x_values[i])
			updated_y.append(y_values[i])

	return updated_x, updated_y

if __name__ == "__main__":

	x_values, y_values = read_points()

	plot_reference_points(x_values, y_values)

