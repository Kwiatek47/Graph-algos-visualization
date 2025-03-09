import pygame

# pygame setup
pygame.init()
pygame.font.init()

# Ustawienie czcionki
my_font = pygame.font.SysFont('Arial', 30)

# Wymiary okna
w, h = 900, 900
pygame.display.set_caption('Algo visualization')
screen = pygame.display.set_mode((w, h))
screen.fill("white")
clock = pygame.time.Clock()
running = True
coursor = pygame.mouse.set_cursor(*pygame.cursors.diamond)

# Kolory
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pozycje i rozmiary przycisków
buttons = {
        "DFS": (250, 20, 70, 50),
        "BFS": (330, 20, 70, 50),
        "Dijkstra": (410, 20, 120, 50),
        "A*": (540, 20, 100, 50),
        "Reset": (680, 20, 120, 50)
}

# Lista przechowująca zaznaczone obszary (kwadraty 50x50px)
selected_squares = []
start_square = (0, 0)
end_square = (0, 0) 

# Menu
def DisplayMenu():
        pygame.draw.line(screen, RED, (0, 100), (w, 100), width=3)

        for text, (x, y, width, height) in buttons.items():
                pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Obramowanie przycisku
                text_surface = my_font.render(text, True, BLACK)
                text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
                screen.blit(text_surface, text_rect)  

def DisplayBoard():
        # Rysowanie szachownicy (linia pozioma)
        for x in range(0, 901, 50): 
                pygame.draw.line(screen, BLACK, (x, 100), (x, 900), width=2)

        # Rysowanie szachownicy (linia pionowa)
        for y in range(100, 901, 50): 
                pygame.draw.line(screen, BLACK, (0, y), (900, y), width=2)

        # Rysowanie zaznaczonych kwadratów
        for square in selected_squares:
                pygame.draw.rect(screen, BLACK, pygame.Rect(square[0], square[1], 50, 50))  # Czarny kwadrat 50x50px
        
        if start_square != (0, 0):
                pygame.draw.rect(screen, (0,128,0), pygame.Rect(start_square[0], start_square[1], 50, 50))
        if end_square != (0, 0):
                pygame.draw.rect(screen, (255,0,0), pygame.Rect(end_square[0], end_square[1], 50, 50))

def mouse_button_events(event):
        global start_square, end_square, selected_squares

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Sprawdź, czy kliknięcie miało miejsce poniżej 100px na osi Y
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_y > 100:  # Jeżeli kliknięcie jest poniżej menu
                        # Oblicz, do którego kwadratu 50x50px zostało kliknięte
                        grid_x = (mouse_x // 50) * 50
                        grid_y = (mouse_y // 50) * 50

                        # Dodaj ten kwadrat do listy zaznaczonych, jeśli jeszcze nie został dodany
                        if (grid_x, grid_y) not in selected_squares:
                                selected_squares.append((grid_x, grid_y))
                else: # Sprawdź, czy kliknięcie miało miejsce w MENU
                        pass
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if start_square == (0, 0):
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if mouse_y > 100:  # Jeżeli kliknięcie jest poniżej menu
                                # Oblicz, do którego kwadratu 50x50px zostało kliknięte
                                grid_x = (mouse_x // 50) * 50
                                grid_y = (mouse_y // 50) * 50
                                start_square = (grid_x, grid_y)
                elif start_square != (0, 0) and end_square == (0, 0):
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if mouse_y > 100:  # Jeżeli kliknięcie jest poniżej menu
                                # Oblicz, do którego kwadratu 50x50px zostało kliknięte
                                grid_x = (mouse_x // 50) * 50
                                grid_y = (mouse_y // 50) * 50
                                if (grid_x, grid_y) != start_square:
                                        end_square = (grid_x, grid_y)

        # Obsługa kliknięcia przycisku "Reset"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                reset_button_x, reset_button_y, reset_button_width, reset_button_height = buttons["Reset"]
                # Sprawdzamy, czy kliknięcie było w przycisk "Reset"
                if (reset_button_x <= mouse_x <= reset_button_x + reset_button_width and
                        reset_button_y <= mouse_y <= reset_button_y + reset_button_height):
                    # Resetujemy wszystkie zmienne do wartości początkowych
                    selected_squares = []
                    start_square = (0, 0)
                    end_square = (0, 0)

# Main Loop
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False 
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        running = False
                        
                mouse_button_events(event)

        screen.fill("white")
        DisplayMenu()
        DisplayBoard()

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

pygame.quit()
