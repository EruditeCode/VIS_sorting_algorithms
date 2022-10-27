"""
Visualisation of Sorting Algorithms
-----------------------------------

Dependencies, Function, Properties
Update this with classes e.g. a sort class
that accepts min, max and number of elements.
The sort_object.frames is the iterable for each frame.
"""

import pygame
from random import randint
from sort_modules import Sort
from sys import exit


def main():
	pygame.init()

	# Initialise variables.
	WINDOW_HEIGHT = 400
	WINDOW_WIDTH = 800
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	clock = pygame.time.Clock()

	# Background and surfaces for interface.
	bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
	bg.fill((20, 20, 20))
	menu = pygame.Surface((180, WINDOW_HEIGHT))
	menu.fill((20, 20, 20))
	disp = pygame.image.load('earth.jpg').convert_alpha()

	# Buttons for sort choice.
	bubble = pygame.Surface((30, 30))
	quick = pygame.Surface((30, 30))
	heap = pygame.Surface((30, 30))
	# Buttons for play/pause and for reset.
	play_btn = pygame.Surface((70, 30))
	reset_btn = pygame.Surface((70, 30))
	reset_btn.fill((60, 60, 60))

	# Initialising a sort object.
	elements, range_min, range_max = 100, 1, 100
	array = [randint(range_min, range_max + 1) for i in range(elements)]
	choice = "bubble"
	sort_obj = Sort(array, choice)
	play = False
	

	# Initialising a counter to iterate over any frames.
	count = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			# Setting up user input features.
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if event.button == 1 and play == False:
					# Check each sort button.
					if in_rect(mouse_pos, 30, 60, 80, 110):
						choice = "bubble"
					if in_rect(mouse_pos, 30, 60, 120, 150):
						choice = "quick"
					if in_rect(mouse_pos, 30, 60, 160, 190):
						choice = "heap"
					if in_rect(mouse_pos, 30, 90, 320, 350):
						# Check the play button.
						play = True
					if in_rect(mouse_pos, 30, 90, 280, 310):
						# Check the reset button.
						array = [randint(range_min, range_max + 1) for i in range(elements)]
						count = 0
						sort_obj = Sort(array, choice)

				elif event.button == 1 and play == True:
					if in_rect(mouse_pos, 30, 90, 320, 350):
						# Check the pause button.
						play = False

		# Displaying the background surface.
		screen.blit(bg, (0, 0))
		screen.blit(menu, (0, 0))
		screen.blit(disp, (180, 0))

		# Selecting color and displaying the sort buttons.
		bubble.fill((60, 60, 60)) if choice == "bubble" else bubble.fill((255, 255, 255))
		quick.fill((60, 60, 60)) if choice == "quick" else quick.fill((255, 255, 255))
		heap.fill((60, 60, 60)) if choice == "heap" else heap.fill((255, 255, 255))
		screen.blit(bubble, (30, 80))
		screen.blit(quick, (30, 120))
		screen.blit(heap, (30, 160))

		# Selecting color and displaying the play/pause button.
		play_btn.fill((162, 10, 10)) if play == True else play_btn.fill((0, 112, 61))
		screen.blit(play_btn, (55, 350))
		# Only show reset if the sort animation is not occuring.
		if play == False:
			screen.blit(reset_btn, (55, 310))

		x = (WINDOW_WIDTH - 182) / len(array)
		MAX_NUM = max(array)
		if play == True:
			if sort_obj.status == True:
				for index, element in enumerate(sort_obj.frames[count]):
					ob_height = (element / MAX_NUM) * (WINDOW_HEIGHT - 50)
					pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(182 + (index * x), WINDOW_HEIGHT - ob_height, x - 2, ob_height))
				if count < len(sort_obj.frames) - 1:
					count += 1
				else:
					play = False
			else:
				sort_obj = Sort(array, choice)
				sort_obj.run_sort()
		if play == False:
			for index, element in enumerate(sort_obj.frames[count]):
				ob_height = (element / MAX_NUM) * (WINDOW_HEIGHT - 50)
				pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(182 + (index * x), WINDOW_HEIGHT - ob_height, x - 2, ob_height))


		pygame.display.update()
		clock.tick(30)

def in_rect(position, x_min, x_max, y_min, y_max):
	if (x_min < position[0] < x_max) and (y_min < position[1] < y_max):
		return True
	return False


if __name__ == "__main__":
	main()
