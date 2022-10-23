"""
Visualisation of Sorting Algorithms
-----------------------------------

Dependencies, Function, Properties
"""

import pygame
from random import randint
from sys import exit


def main():
	pygame.init()

	# Initialise variables.
	WINDOW_HEIGHT = 400
	WINDOW_WIDTH = 800
	sort_choice = "bubble"
	number_elements = 50
	range_min = 1
	range_max = 10
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

		if play == True:
			if sort == True:
				# Display the frames.
				pass
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
	sort = False
	frames = []

def run_sort(array, sort_choice, frames):
	pass


if __name__ == "__main__":
	main()
