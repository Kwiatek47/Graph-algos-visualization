import pygame
import sys
import os

# Add the dfs folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dfs')))

from dfs import dfs, generate_dfs_trace, Valid

# Initialize pygame and font modules
pygame.init()
pygame.font.init()

# Set up the font for displaying text
my_font = pygame.font.SysFont('Arial', 30)

# Window dimensions
w, h = 900, 900
pygame.display.set_caption('Algo visualization')
screen = pygame.display.set_mode((w, h))
screen.fill("white")
clock = pygame.time.Clock()
running = True
pygame.mouse.set_cursor(*pygame.cursors.diamond)

# Define some colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Button definitions with positions and sizes
buttons = {
	"DFS": (250, 20, 70, 50),
	"BFS": (330, 20, 70, 50),
	"Dijkstra": (410, 20, 120, 50),
	"A*": (540, 20, 100, 50),
	"Reset": (680, 20, 120, 50)
}

algorithms = {
	"DFS": False,
	"BFS": False,
	"Dijkstra": False,
	"A(star)": False
}

# List for storing clicked grid squares (each square is 50x50px)
selected_squares = []
start_square = (0, 0)
end_square = (0, 0)

# Variables for animating the DFS path
dfs_path = []
dfs_index = 0
animating_dfs = False
animation_delay = 100  # Delay in milliseconds between steps
last_update_time = 0

# Draw the menu with buttons
def DisplayMenu():
	pygame.draw.line(screen, RED, (0, 100), (w, 100), width=3)  # Draw a separator line
	for text, (x, y, width, height) in buttons.items():
		pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Draw button border
		text_surface = my_font.render(text, True, BLACK)
		text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
		screen.blit(text_surface, text_rect)

# Draw the grid and any selected squares
def DisplayBoard():
	# Draw vertical grid lines
	for x in range(0, 901, 50):
		pygame.draw.line(screen, BLACK, (x, 100), (x, 900), width=2)
	# Draw horizontal grid lines
	for y in range(100, 901, 50):
		pygame.draw.line(screen, BLACK, (0, y), (900, y), width=2)
	
	# Draw each square that has been clicked on
	for square in selected_squares:
		pygame.draw.rect(screen, BLACK, pygame.Rect(square[0], square[1], 50, 50))
	
	# Draw the start square (green) and end square (red) if they are set
	if start_square != (0, 0):
		pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(start_square[0], start_square[1], 50, 50))
	if end_square != (0, 0):
		pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(end_square[0], end_square[1], 50, 50))

# Draw the DFS path incrementally
def print_path(vis):
	for (dx, dy) in vis:
		pygame.draw.rect(screen, (255, 160, 0), pygame.Rect(dx, dy, 50, 50))

# Start the DFS animation by generating the DFS trace and resetting animation parameters
def DFS():
	global dfs_path, dfs_index, animating_dfs, last_update_time
	dfs_path = generate_dfs_trace(start_square, end_square, selected_squares)
	dfs_index = 0
	animating_dfs = True
	last_update_time = pygame.time.get_ticks()

def BFS():
	print("BFS")

def DIJKSTRA():
	print("Dijkstra")

def ASTAR():
	print("A*")

# Process mouse events for grid selection and button clicks
def mouse_button_events(event):
	global start_square, end_square, selected_squares
	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_y > 100:  # Clicked on the grid
			grid_x = (mouse_x // 50) * 50
			grid_y = (mouse_y // 50) * 50
			if (grid_x, grid_y) not in selected_squares:
				selected_squares.append((grid_x, grid_y))
		else:  # Clicked on the menu buttons
			grid_x = (mouse_x // 100) * 100
			if grid_x == 200:
				DFS()
			elif grid_x == 300:
				BFS()
			elif grid_x == 400:
				DIJKSTRA()
			elif grid_x == 500:
				ASTAR()
	
	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if start_square == (0, 0) and mouse_y > 100:
			grid_x = (mouse_x // 50) * 50
			grid_y = (mouse_y // 50) * 50
			start_square = (grid_x, grid_y)
		elif start_square != (0, 0) and end_square == (0, 0) and mouse_y > 100:
			grid_x = (mouse_x // 50) * 50
			grid_y = (mouse_y // 50) * 50
			if (grid_x, grid_y) != start_square:
				end_square = (grid_x, grid_y)
	
	# Handle click on the "Reset" button to clear the board
	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		reset_button_x, reset_button_y, reset_button_width, reset_button_height = buttons["Reset"]
		if (reset_button_x <= mouse_x <= reset_button_x + reset_button_width and
				reset_button_y <= mouse_y <= reset_button_y + reset_button_height):
			selected_squares.clear()
			start_square = (0, 0)
			end_square = (0, 0)

# Main loop
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			running = False
		mouse_button_events(event)
	
	# Clear the screen each frame
	screen.fill("white")
	DisplayMenu()
	DisplayBoard()
	
	# Update DFS animation: show the path one step at a time
	if animating_dfs:
		current_time = pygame.time.get_ticks()
		if current_time - last_update_time > animation_delay:
			dfs_index += 1
			last_update_time = current_time
			if dfs_index > len(dfs_path):
				animating_dfs = False
		# Draw only the part of the DFS path that is ready
		print_path(dfs_path[:dfs_index])
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
