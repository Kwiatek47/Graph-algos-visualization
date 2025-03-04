import pygame

# pygame setup
pygame.init()
pygame.font.init()

# Ustawienie czcionki
my_font = pygame.font.SysFont('Arial', 30)

# Wymiary okna
w, h = 900, 900
screen = pygame.display.set_mode((w, h))
screen.fill("white")
clock = pygame.time.Clock()
running = True
coursor = pygame.mouse.set_cursor(*pygame.cursors.diamond)

# Menu
def DisplayMenu():
        pygame.draw.line(screen, (255, 0, 0), (0, 100), (w, 100), width=3)
        
        dfs_surface = my_font.render("DFS", True, (0, 0, 0))
        bfs_surface = my_font.render("BFS", True, (0, 0, 0))
        dijkstra_surface = my_font.render("Dijkstra", True, (0, 0, 0))
        astar_surface = my_font.render("A*(star)", True, (0, 0, 0))

        x = 250
        screen.blit(dfs_surface, (x + 10, 30))  
        screen.blit(bfs_surface, (x + 90, 30))  
        screen.blit(dijkstra_surface, (x + 165, 30))  
        screen.blit(astar_surface, (x + 270, 30))  

def DisplayBoard():
        # Game, board, algos visualization, etc.
        pass

# Main Loop
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False 
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        running = False

        screen.fill("white")  # Czyszczenie ekranu przed rysowaniem
        DisplayMenu()
        DisplayBoard()

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

pygame.quit()
