"""
Visualisation of Sorting Algorithms
-----------------------------------

Dependencies, Function, Properties
"""

import pygame
from random import randint
from sys import exit

pivots = []


def main():
	pygame.init()

	# Initialise variables.
	WINDOW_HEIGHT = 400
	WINDOW_WIDTH = 800
	sort_choice = "bubble"
	number_elements = 100
	range_min = 1
	range_max = 50
	play = False
	sort = False
	frames = []
	array = [randint(range_min, range_max + 1) for i in range(number_elements)]

	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	clock = pygame.time.Clock()

	bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
	bg.fill((20, 20, 20))
	menu = pygame.Surface((180, WINDOW_HEIGHT))
	menu.fill((150, 150, 150))
	disp = pygame.image.load('earth.jpg').convert_alpha()

	# Buttons for sort choice.
	bubble = pygame.Surface((30, 30))
	quick = pygame.Surface((30, 30))
	heap = pygame.Surface((30, 30))

	# Button for play.
	play_btn = pygame.Surface((60, 30))
	play_btn.fill("white")


	count = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if event.button == 1 and play == False:
					# Check each sort button.
					if in_rect(mouse_pos, 30, 60, 100, 130):
						sort_choice = "bubble"
					if in_rect(mouse_pos, 30, 60, 140, 170):
						sort_choice = "quick"
					if in_rect(mouse_pos, 30, 60, 180, 210):
						sort_choice = "heap"
					if in_rect(mouse_pos, 30, 90, 320, 350):
						play = True
				if event.button == 1 and play == True:
					if in_rect(mouse_pos, 30, 90, 320, 350):
						count = 0
						sort = False
						frames = []
						array = [randint(range_min, range_max + 1) for i in range(number_elements)]

		# Displaying the background surface.
		screen.blit(bg, (0, 0))
		screen.blit(menu, (0, 0))
		screen.blit(disp, (180, 0))

		if sort_choice == "bubble":
			bubble.fill((40, 40, 40))
			quick.fill((200, 200, 200))
			heap.fill((200, 200, 200))
		elif sort_choice == "quick":
			bubble.fill((200, 200, 200))
			quick.fill((40, 40, 40))
			heap.fill((200, 200, 200))
		elif sort_choice == "heap":
			bubble.fill((200, 200, 200))
			quick.fill((200, 200, 200))
			heap.fill((40, 40, 40))

		screen.blit(bubble, (30, 100))
		screen.blit(quick, (30, 140))
		screen.blit(heap, (30, 180))

		screen.blit(play_btn, (30, 320))

		if play == True:
			if sort == True:
				x = (WINDOW_WIDTH - 182) / len(array)
				MAX_NUM = max(array)
				for index, element in enumerate(frames[count]):
					ob_height = (element / MAX_NUM) * (WINDOW_HEIGHT - 50)
					pygame.draw.rect(screen, 'White', pygame.Rect(182 + (index * x), WINDOW_HEIGHT - ob_height, x - 2, ob_height))
				if count < len(frames) - 1:
					count += 1
			else:
				frames = run_sort(array, sort_choice, frames)
				sort = True

		pygame.display.update()
		clock.tick(30)

def in_rect(position, x_min, x_max, y_min, y_max):
	if (x_min < position[0] < x_max) and (y_min < position[1] < y_max):
		return True
	return False

def reset():
	count = 0
	sort = False
	frames = []

def run_sort(array, sort_choice, frames):
	if sort_choice == "bubble":
		frames = [array.copy()]
		sort = False
		while sort == False:
			sort = True
			# Iterate through the list of numbers and compare pairs.
			for i in range(0, len(array) - 1):
				if array[i] > array[i + 1]:
					array[i], array[i + 1] = array[i + 1], array[i]
					sort = False
					frames.append(array.copy())
		return frames
	elif sort_choice == "quick":
		initial_array = array.copy()
		frames.append(initial_array)
		array = quick_sort(array)
		# Use pivots to generate frames.
		# NEED TO IMPROVE LOGIC FOR EACH COMPARISON FRAME.
		for pivot in pivots:
			low, same, high = [], [], []
			for value in frames[-1]:
				if value < pivot:
					low.append(value)
				elif value == pivot:
					same.append(value)
				elif value > pivot:
					high.append(value)
			frame = low + same + high
			frames.append(frame)
		return frames


	elif sort_choice == "heap":
		pass


def quick_sort(array):
	if len(array) <= 1:
		return array

	pivot_index = randint(0, len(array) - 1)
	pivot = array[pivot_index]
	pivots.append(pivot)

	lesser, same, greater = [], [], []

	for element in array:
		if element == pivot:
			same.append(element)
		elif element < pivot:
			lesser.append(element)
		elif element > pivot:
			greater.append(element)

	return quick_sort(lesser) + same + quick_sort(greater)


if __name__ == "__main__":
	main()
