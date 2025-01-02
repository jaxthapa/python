#Initialize pygame
pygame.int()

#Screen dimensions
WIDTH, HEIGHT = 800, 600
screen =
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

#player settings
player_width, player-height = 100,20
player_x =WIDTH // 2 -
player_width //2
player_y =HEIGHT - player_height -10
player_speed =10

#Falling object settings
object_width, object_height = 30, 30
object_x = random.randint(0, WIDTH -
object-width)                          



