import numpy as np
import pandas 
import sys
import os
from collections import OrderedDict
import matplotlib.pyplot as plt
import math
from read_ref_points import *

class Points2D:

	def __init__(self):
		self.x = 0
		self.y = 0
		self.points = (self.x, self.y)

class Spline2D:

	def __init__(self, points2d):
		self.spline2d = []


def GetSplinePoint(t, x_cordinates, y_cordinates):

	original_t = t

	p1 = math.floor(t) + 1
	p2 = p1 + 1
	p3 = p2 + 1
	p0 = p1 - 1

	t = t - math.floor(t)

	tt = t * t
	ttt = tt * t

	q1 = -ttt + 2.0 * tt - t 
	q2 = 3.0 * ttt - 5.0 * tt + 2.0
	q3 = -3.0 * ttt + 4.0 * tt + t
	q4 = ttt - tt 

	# q1 = -3.0 * tt + 4.0*t - 1
	# q2 = 9.0*tt - 10.0*t
	# q3 = -9.0*tt + 8.0*t + 1.0
	# q4 = 3.0*tt - 2.0*t

	print("P values : {} | {} | {} | {}".format(p0, p1, p2, p3))
	print("Data : {} | P0 {} {} | P1 {} {} | P2 {} {} | P3 {} {}".format(original_t, x_cordinates[p0], y_cordinates[p0], x_cordinates[p1], y_cordinates[p1], x_cordinates[p2], y_cordinates[p2], x_cordinates[p3], y_cordinates[p3]))

	tx = 0.5 * (x_cordinates[p0] * q1 + x_cordinates[p1] * q2 + x_cordinates[p2] * q3 + x_cordinates[p3] * q4)
	ty = 0.5 * (y_cordinates[p0] * q1 + y_cordinates[p1] * q2 + y_cordinates[p2] * q3 + y_cordinates[p3] * q4)

	#print("P values ")

	return (tx, ty)


if __name__ == "__main__":

	# Points - X Y 
	# points2D = OrderedDict()

	# vector of Points2D 
	# spline2D = OrderedDict()

	points2d = Points2D()
	print(points2d.x)
	print(points2d.y)
	print(points2d.points)

	#spline2d = Spline2D()

	#control_points = [(10, 41), (40, 81), (70, 81), (100, 71), (150, 41)]

	ref_x, ref_y = read_points()
	sampled_ref_x, sampled_ref_y = sample_points(ref_x, ref_y)
	control_points = order_points(sampled_ref_x, sampled_ref_y)

	#control_points = [(10, 41), (20, 61), (30, 61), (40, 81), (50, 91), (60, 61), (70, 31), (80, 41), (90, 61), (100, 81)]

	x_cordinates = [x[0] for x in control_points]
	y_cordinates = [x[1] for x in control_points]

	#print(x_cordinates)
	#print(y_cordinates)

	# plt.scatter(x_cordinates, y_cordinates)
	# plt.show()

	#t_value = [x*0.01 for x in range(0, 100)]
	#t_value = [x*0.01 for x in range(0, len(control_points))]
	#t_value = [x*0.005 for x in range(0, len(control_points) - 3)]
	#t_value = np.arange(0, (len(control_points) - 0), 0.05)  # Working
	#t_value = list(np.asarray(t_value)) # Working

	#print("T Values : {}".format(t_value))

	final_points = []
	counter = 0

	#for each_t in t_value:

	t_count = 0

	while t_count < len(control_points) - 3:

		(tx, ty) = GetSplinePoint(t_count, x_cordinates, y_cordinates)
		spline_points = (tx, ty)
		#print(tx, ty)
		final_points.append(spline_points)
		counter += 1

		t_count = t_count + 0.005

	#print(final_points)
	print("counter : {}".format(counter))

	final_x_cordinates = [x[0] for x in final_points]
	final_y_cordinates = [x[1] for x in final_points]

	#plt.scatter(final_x_cordinates, final_y_cordinates)
	#plt.show()

	fig, axes = plt.subplots(nrows = 1, ncols = 2)
	axes[0].scatter(final_x_cordinates, final_y_cordinates)
	axes[0].scatter(x_cordinates, y_cordinates)

	axes[0].set_title("Raw_points + Smoothed_points")
	#axes[1].scatter(final_x_cordinates, final_y_cordinates)
	#axes[1].set_title("Smoothed_points")
	plt.show()