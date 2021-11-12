import pygame
import sys
from builder import Builder
from data.gamedata import GameData




# initializes pygame
pygame.init()
pygame.display.set_caption(GameData.game_title)
builder = Builder()
builder.grid_init()



#Game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not builder.game_over:
			mouseX = event.pos[0]
			mouseY = event.pos[1]

			# Transforms mouse coordinates to grid coordinates
			h_axis = int(mouseY // GameData.square_size)
			v_axis = int(mouseX // GameData.square_size)

			if builder.check_tile_availability(h_axis, v_axis):
				builder.draw_player_symbol(h_axis, v_axis, builder.player)
				if builder.winning_event(builder.player):
					game_over = True
				builder.player = builder.player % 2 + 1

				builder.draw_player_symbols()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				builder.game_restart()
				game_over = False

	pygame.display.update()