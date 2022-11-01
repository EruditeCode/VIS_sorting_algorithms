# Navigation functions to support the Visual Sorts program.

def in_rect(position, x_min, x_max, y_min, y_max):
	if (x_min < position[0] < x_max) and (y_min < position[1] < y_max):
		return True
	return False

def in_circle(point, circle_centre, circle_radius):
	if euclidean_distance(point, circle_centre) <= circle_radius:
		return True
	return False
	
def euclidean_distance(point_1, point_2):
	s = 0.0
	for i in range(len(point_1)):
		s += ((point_1[i] - point_2[i]) ** 2)
	return s ** 0.5
