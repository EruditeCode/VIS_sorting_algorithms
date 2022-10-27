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
	pygame.display.set_caption("Visual Sorts")
	clock = pygame.time.Clock()
	title_font = pygame.font.Font('LCD-U___.ttf', 28)
	txt_font = pygame.font.Font('LCD-U___.ttf', 18)

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

	# Creating the text objects.
	title = title_font.render('Visual Sorts', True, (255, 255, 255))
	titleRect = title.get_rect(topleft=(10,20))
	bubble_txt = txt_font.render('Bubble Sort', True, (255, 255, 255))
	bubbleRect = bubble_txt.get_rect(topleft=(63,86))
	quick_txt = txt_font.render('Quick Sort', True, (255, 255, 255))
	quickRect = quick_txt.get_rect(topleft=(63,126))
	heap_txt = txt_font.render('Heap Sort', True, (255, 255, 255))
	heapRect = heap_txt.get_rect(topleft=(63,166))
	play_txt = txt_font.render('Play', True, (255, 255, 255))
	playRect = play_txt.get_rect(topleft=(70,356))
	pause_txt = txt_font.render('Pause', True, (255, 255, 255))
	pauseRect = pause_txt.get_rect(topleft=(65,356))
	reset_txt = txt_font.render('Reset', True, (255, 255, 255))
	resetRect = reset_txt.get_rect(topleft=(67,317))

	# Initialising a sort object.
	elements, range_min, range_max = 100, 1, 100
	array = [randint(range_min, range_max + 1) for i in range(elements)]
	choice = "bubble"
	sort_obj = Sort(array, choice)
	play = False
	circle_pos_x = 42 + (elements - 10) // 2
	circle_pos = (circle_pos_x, 266)
	mouse_sticky = False
	

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
					if in_rect(mouse_pos, 25, 55, 80, 110):
						choice = "bubble"
					if in_rect(mouse_pos, 25, 55, 120, 150):
						choice = "quick"
					if in_rect(mouse_pos, 25, 55, 160, 190):
						choice = "heap"
					if in_circle(mouse_pos, circle_pos, 7):
						mouse_sticky = True
					if in_rect(mouse_pos, 55, 125, 350, 380):
						# Check the play button.
						play = True
					if in_rect(mouse_pos, 55, 125, 310, 340):
						# Check the reset button.
						array = [randint(range_min, range_max + 1) for i in range(elements)]
						count = 0
						sort_obj = Sort(array, choice)

				elif event.button == 1 and play == True:
					if in_rect(mouse_pos, 55, 125, 350, 380):
						# Check the pause button.
						play = False

			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					mouse_sticky = False

		42 + (elements - 10) // 2
		if mouse_sticky == True:
			mouse_pos = pygame.mouse.get_pos()
			if mouse_pos[0] > 137:
				circle_pos = (137, 266)
			elif mouse_pos[0] < 42:
				circle_pos = (42, 266)
			else:
				circle_pos = (mouse_pos[0], 266)
			elements = ((circle_pos[0] - 42) * 2) + 10

		# Displaying the background surface.
		screen.blit(bg, (0, 0))
		screen.blit(menu, (0, 0))
		screen.blit(disp, (180, 0))

		# Selecting color and displaying the sort buttons.
		bubble.fill((0, 86, 62)) if choice == "bubble" else bubble.fill((255, 255, 255))
		quick.fill((0, 86, 62)) if choice == "quick" else quick.fill((255, 255, 255))
		heap.fill((0, 86, 62)) if choice == "heap" else heap.fill((255, 255, 255))
		screen.blit(bubble, (25, 80))
		screen.blit(quick, (25, 120))
		screen.blit(heap, (25, 160))

		# Selecting color and displaying the play/pause button.
		play_btn.fill((255, 127, 1)) if play == True else play_btn.fill((0, 86, 62))
		screen.blit(play_btn, (55, 350))
		# Only show reset if the sort animation is not occuring.
		if play == False:
			screen.blit(reset_btn, (55, 310))

		# Creating the slider widget.
		circle_pos_x = 42 + (elements - 10) // 2
		circle_pos = (circle_pos_x, 266)
		pygame.draw.line(screen, (255, 255, 255), (42,265), (137,265), 4)
		pygame.draw.circle(screen, (0, 86, 62), circle_pos, 7)

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

		# Create the dynamic text for number of elements.
		n_elements = f"Elements: {elements}"
		elements_txt = txt_font.render(n_elements, True, (255, 255, 255))
		elementsRect = elements_txt.get_rect(topleft=(35,225))
		screen.blit(elements_txt, elementsRect)

		# Displaying all the text.
		screen.blit(title, titleRect)
		screen.blit(bubble_txt, bubbleRect)
		screen.blit(quick_txt, quickRect)
		screen.blit(heap_txt, heapRect)
		if play == False:
			screen.blit(play_txt, playRect)
			screen.blit(reset_txt, resetRect)
		if play == True:
			screen.blit(pause_txt, pauseRect)


		pygame.display.update()
		clock.tick(30)

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


if __name__ == "__main__":
	main()
