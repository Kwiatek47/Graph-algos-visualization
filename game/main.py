import pygame

# pygame setup
pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Arial', 30)
screen = pygame.display.set_mode((1280, 720))
screen.fill("white")
clock = pygame.time.Clock()
running = True

def func():
        return 'Text...'

while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        running = False

        # RENDER YOUR GAME HERE

        text = func()
        text_surface = my_font.render(text, False, (0,0,0))
        screen.blit(text_surface, (1280 / 2, 0))

        pygame.draw.lines(screen, (0, 0, 0), False, [(0, 1), (0, 3), (2, 4), (10, 200)], 2)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()