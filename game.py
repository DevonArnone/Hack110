import pygame
import random
import sys


# Initialize pygame
pygame.init()


# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump110 - Side-to-Side Platformer")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


# Game variables
player_size = 50
platform_width, platform_height = 70, 15
jump_power = -15
gravity = 1
move_speed = 5
score = 0
lives = 2  # Number of lives
is_jumping = False


# Player setup
player = pygame.Rect(WIDTH // 2, HEIGHT - player_size - 100, player_size, player_size)
player_velocity_y = 0


# Platforms setup (horizontal placement)
platforms = [
   pygame.Rect(random.randint(0, WIDTH - platform_width), HEIGHT - (i * 100), platform_width, platform_height)
   for i in range(6)
]


# Font setup for score and lives
font = pygame.font.Font(None, 36)


def game_loop():
   global player_velocity_y, score, is_jumping, lives


   running = True
   clock = pygame.time.Clock()


   while running:
       screen.fill(BLUE)


       # Event handling
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False


       # Player movement
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           player.x -= move_speed
       if keys[pygame.K_RIGHT]:
           player.x += move_speed


       # Check for platform collision and update score
       player_velocity_y += gravity
       player.y += player_velocity_y


       # Make player "jump" when on platform
       on_platform = False
       for platform in platforms:
           if player.colliderect(platform) and player_velocity_y > 0:
               player_velocity_y = jump_power
               score += 1
               on_platform = True
               break


       # Reset player if they fall below screen and reduce lives
       if player.y > HEIGHT:
           lives -= 1
           player.x, player.y = WIDTH // 2, HEIGHT - player_size - 100
           player_velocity_y = 0
           if lives <= 0:
               print("Game Over")
               running = False


       # Draw platforms
       for platform in platforms:
           pygame.draw.rect(screen, BLACK, platform)


       # Draw player
       pygame.draw.rect(screen, WHITE, player)


       # Draw score and lives
       score_text = font.render(f"Score: {score}", True, BLACK)
       lives_text = font.render(f"Lives: {lives}", True, BLACK)
       screen.blit(score_text, (10, 10))
       screen.blit(lives_text, (WIDTH - 100, 10))


       pygame.display.flip()
       clock.tick(30)


game_loop()


pygame.quit()
sys.exit()





