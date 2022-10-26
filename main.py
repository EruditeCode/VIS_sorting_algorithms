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
	sort_choice = "bubble"
	number_elements = 100
	range_min = 1
	range_max = 50
	play = False
	sort = False
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
						array = [randint(range_min, range_max + 1) for i in range(number_elements)]
						count = 0
						sort = False
						sort_obj = Sort(array, sort_choice)

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
				for index, element in enumerate(sort_obj.frames[count]):
					ob_height = (element / MAX_NUM) * (WINDOW_HEIGHT - 50)
					pygame.draw.rect(screen, 'White', pygame.Rect(182 + (index * x), WINDOW_HEIGHT - ob_height, x - 2, ob_height))
				if count < len(sort_obj.frames) - 1:
					count += 1
			else:
				sort_obj = Sort(array, sort_choice)
				sort_obj.run_sort()
				sort = True

		pygame.display.update()
		clock.tick(30)

def in_rect(position, x_min, x_max, y_min, y_max):
	if (x_min < position[0] < x_max) and (y_min < position[1] < y_max):
		return True
	return False


if __name__ == "__main__":
	main()
