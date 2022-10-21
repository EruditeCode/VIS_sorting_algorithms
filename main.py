"""
Visualisation of Sorting Algorithms
-----------------------------------

Dependencies, Function, Properties
"""

import pygame
from sys import exit

# Initialise variables.
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 800
user_sort = "bubble"
user_elements = 50
user_range_low = 1
user_range_high = 10
play = False


def main():
	pygame.init()
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	clock = pygame.time.Clock()

	bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
	bg.fill((20, 20, 20))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		# Displaying the background surface.
		screen.blit(bg, (0, 0))


if __name__ == "__main__":
	main()
