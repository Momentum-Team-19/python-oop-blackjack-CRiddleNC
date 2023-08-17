import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BORDER_THICKNESS = 10
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DIAMOND_WIDTH = 40
DIAMOND_HEIGHT = 20
MOVEMENT_SPEED = 4

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circuit Racer")

# Load background image
background_image = pygame.image.load("images/circut-background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Create a list to store visited points for the trail
trail_points = []

# Store the current movement direction
current_direction = None

# Initial oval position
oval_x = WIDTH // 2 - DIAMOND_WIDTH // 2
oval_y = HEIGHT // 2 - DIAMOND_HEIGHT // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle arrow key input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        current_direction = pygame.K_LEFT
    elif keys[pygame.K_RIGHT]:
        current_direction = pygame.K_RIGHT
    elif keys[pygame.K_UP]:
        current_direction = pygame.K_UP
    elif keys[pygame.K_DOWN]:
        current_direction = pygame.K_DOWN

    # Clear the screen
    screen.blit(background_image, (0, 0))

    # Update the polygon position based on the direction
    if current_direction == pygame.K_LEFT:
        oval_x -= MOVEMENT_SPEED
    elif current_direction == pygame.K_RIGHT:
        oval_x += MOVEMENT_SPEED
    elif current_direction == pygame.K_UP:
        oval_y -= MOVEMENT_SPEED
    elif current_direction == pygame.K_DOWN:
        oval_y += MOVEMENT_SPEED

    # Calculate the rotation angle based on the current direction
    if current_direction == pygame.K_LEFT:
        rotation_angle = 0
    elif current_direction == pygame.K_RIGHT:
        rotation_angle = math.pi
    elif current_direction == pygame.K_UP:
        rotation_angle = -math.pi / 2
    elif current_direction == pygame.K_DOWN:
        rotation_angle = math.pi / 2
    else:
        rotation_angle = 0

    # Calculate rotated vertices for the split oval
    half_oval_width = DIAMOND_WIDTH // 2
    half_oval_height = DIAMOND_HEIGHT // 2

    left_half_vertices = [
        (oval_x, oval_y + half_oval_height),
        (oval_x + half_oval_width, oval_y),
        (oval_x + half_oval_width, oval_y + DIAMOND_HEIGHT)
    ]

    right_half_vertices = [
        (oval_x + half_oval_width, oval_y),
        (oval_x + DIAMOND_WIDTH, oval_y + half_oval_height),
        (oval_x + half_oval_width, oval_y + DIAMOND_HEIGHT)
    ]

    rotated_left_vertices = [
        (
            oval_x + half_oval_width + math.cos(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
            - math.sin(rotation_angle) * (vertex[1] - oval_y - half_oval_height),
            oval_y + half_oval_height + math.sin(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
            + math.cos(rotation_angle) * (vertex[1] - oval_y - half_oval_height)
        )
        for vertex in left_half_vertices
    ]

    rotated_right_vertices = [
        (
            oval_x + half_oval_width + math.cos(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
            - math.sin(rotation_angle) * (vertex[1] - oval_y - half_oval_height),
            oval_y + half_oval_height + math.sin(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
            + math.cos(rotation_angle) * (vertex[1] - oval_y - half_oval_height)
        )
        for vertex in right_half_vertices
    ]

    # Draw the polygon and trail
    pygame.draw.polygon(screen, RED, rotated_left_vertices)
    pygame.draw.polygon(screen, GREEN, rotated_right_vertices)
    if len(trail_points) > 1:
        pygame.draw.lines(screen, GREEN, False, trail_points, 2)

    # Update the display
    pygame.display.update()

    # Add the current oval position to the trail points
    trail_points.append((oval_x + DIAMOND_WIDTH // 2, oval_y + DIAMOND_HEIGHT // 2))

    # Check collision with the border
    if (
        BORDER_THICKNESS <= oval_x <= WIDTH - DIAMOND_WIDTH - BORDER_THICKNESS and
        BORDER_THICKNESS <= oval_y <= HEIGHT - DIAMOND_HEIGHT - BORDER_THICKNESS
    ):
        collides_with_trail = any(
            (oval_x + DIAMOND_WIDTH // 2, oval_y + DIAMOND_HEIGHT // 2) == point
            for point in trail_points
        )

        if not collides_with_trail:
            # Update the display
            pygame.display.update()
    else:
        running = False  # Exit the game when the polygon can no longer move

# Clean up
pygame.quit()
sys.exit()

# import pygame
# import sys
# import math

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 800, 600
# BORDER_THICKNESS = 10
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# DIAMOND_WIDTH = 40
# DIAMOND_HEIGHT = 20
# MOVEMENT_SPEED = 4

# # Create the window
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Circuit Racer")

# # Initial oval position
# oval_x = WIDTH // 2 - DIAMOND_WIDTH // 2
# oval_y = HEIGHT // 2 - DIAMOND_HEIGHT // 2

# # Create a list to store visited points for the trail
# trail_points = []

# # Store the current movement direction
# current_direction = None

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Handle arrow key input
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         current_direction = pygame.K_LEFT
#     elif keys[pygame.K_RIGHT]:
#         current_direction = pygame.K_RIGHT
#     elif keys[pygame.K_UP]:
#         current_direction = pygame.K_UP
#     elif keys[pygame.K_DOWN]:
#         current_direction = pygame.K_DOWN

#     if current_direction:
#         if current_direction == pygame.K_LEFT:
#             oval_x -= MOVEMENT_SPEED
#         elif current_direction == pygame.K_RIGHT:
#             oval_x += MOVEMENT_SPEED
#         elif current_direction == pygame.K_UP:
#             oval_y -= MOVEMENT_SPEED
#         elif current_direction == pygame.K_DOWN:
#             oval_y += MOVEMENT_SPEED

#     # Check collision with the border
#     if (
#         BORDER_THICKNESS <= oval_x <= WIDTH - DIAMOND_WIDTH - BORDER_THICKNESS and
#         BORDER_THICKNESS <= oval_y <= HEIGHT - DIAMOND_HEIGHT - BORDER_THICKNESS
#     ):
#         collides_with_trail = any(
#             (oval_x + DIAMOND_WIDTH // 2, oval_y + DIAMOND_HEIGHT // 2) == point
#             for point in trail_points
#         )

#         if not collides_with_trail:
#             # Clear the screen
#             screen.fill((0, 0, 0))

#             # Calculate rotated vertices for the split oval
#             rotation_angle = 0
#             half_oval_width = DIAMOND_WIDTH // 2
#             half_oval_height = DIAMOND_HEIGHT // 2

#             left_half_vertices = [
#                 (oval_x, oval_y + half_oval_height),
#                 (oval_x + half_oval_width, oval_y),
#                 (oval_x + half_oval_width, oval_y + DIAMOND_HEIGHT)
#             ]

#             right_half_vertices = [
#                 (oval_x + half_oval_width, oval_y),
#                 (oval_x + DIAMOND_WIDTH, oval_y + half_oval_height),
#                 (oval_x + half_oval_width, oval_y + DIAMOND_HEIGHT)
#             ]

#             rotated_left_vertices = [
#                 (
#                     oval_x + half_oval_width + math.cos(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#                     - math.sin(rotation_angle) * (vertex[1] - oval_y - half_oval_height),
#                     oval_y + half_oval_height + math.sin(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#                     + math.cos(rotation_angle) * (vertex[1] - oval_y - half_oval_height)
#                 )
#                 for vertex in left_half_vertices
#             ]

#             rotated_right_vertices = [
#                 (
#                     oval_x + half_oval_width + math.cos(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#                     - math.sin(rotation_angle) * (vertex[1] - oval_y - half_oval_height),
#                     oval_y + half_oval_height + math.sin(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#                     + math.cos(rotation_angle) * (vertex[1] - oval_y - half_oval_height)
#                 )
#                 for vertex in right_half_vertices
#             ]

#             # Draw the polygon and trail
#             pygame.draw.polygon(screen, RED, rotated_left_vertices)
#             pygame.draw.polygon(screen, GREEN, rotated_right_vertices)
#             if len(trail_points) > 1:
#                 pygame.draw.lines(screen, GREEN, False, trail_points, 2)

#             # Update the display
#             pygame.display.update()
            
#             # Add the current oval position to the trail points
#             trail_points.append((oval_x + DIAMOND_WIDTH // 2, oval_y + DIAMOND_HEIGHT // 2))
#     else:
#         running = False  # Exit the game when the polygon can no longer move

# # Clean up
# pygame.quit()
# sys.exit()

# import pygame
# from pygame import mixer
# import sys
# import math

# # Initialize Pygame
# pygame.init()
# mixer.init()  # Initialize the mixer

# # Constants
# WIDTH, HEIGHT = 800, 600
# BORDER_THICKNESS = 10
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# DIAMOND_WIDTH = 40  # Width of the diamond's bounding box
# DIAMOND_HEIGHT = 20  # Height of the diamond's bounding box
# MOVEMENT_SPEED = 4

# # Create the window
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Move the Rotating Oval")

# # Load background image
# background_image = pygame.image.load("images/circut-background.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# # Darken the background image
# darker_factor = 0.2  # Adjust this value to make the image darker
# darkened_background = pygame.Surface((WIDTH, HEIGHT))
# darkened_background.blit(background_image, (0, 0))
# darkened_background.set_alpha(int(255 * darker_factor))
# background_image = darkened_background

# # Initial oval position
# oval_x = WIDTH // 2 - DIAMOND_WIDTH // 2
# oval_y = HEIGHT // 2 - DIAMOND_HEIGHT // 2

# # Create a list to store visited points for the trail
# trail_points = []

# # Store the current movement direction
# current_direction = None

# # Load and play the music
# music_path = "music/Song1-Motor-Skills.mp3"
# pygame.mixer.music.load(music_path)
# pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Handle arrow key input
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         current_direction = pygame.K_LEFT
#     elif keys[pygame.K_RIGHT]:
#         current_direction = pygame.K_RIGHT
#     elif keys[pygame.K_UP]:
#         current_direction = pygame.K_UP
#     elif keys[pygame.K_DOWN]:
#         current_direction = pygame.K_DOWN
#     else:
#         current_direction = None

#     if current_direction == pygame.K_LEFT:
#         new_oval_x = oval_x - MOVEMENT_SPEED
#         new_oval_y = oval_y
#     elif current_direction == pygame.K_RIGHT:
#         new_oval_x = oval_x + MOVEMENT_SPEED
#         new_oval_y = oval_y
#     elif current_direction == pygame.K_UP:
#         new_oval_x = oval_x
#         new_oval_y = oval_y - MOVEMENT_SPEED
#     elif current_direction == pygame.K_DOWN:
#         new_oval_x = oval_x
#         new_oval_y = oval_y + MOVEMENT_SPEED
#     else:
#         new_oval_x = oval_x
#         new_oval_y = oval_y

#     # Check collision with the border
#     if (
#         BORDER_THICKNESS <= new_oval_x <= WIDTH - DIAMOND_WIDTH - BORDER_THICKNESS and
#         BORDER_THICKNESS <= new_oval_y <= HEIGHT - DIAMOND_HEIGHT - BORDER_THICKNESS
#     ):
#         # Check collision with the green trail
#         collides_with_trail = any(
#             (new_oval_x + DIAMOND_WIDTH // 2, new_oval_y + DIAMOND_HEIGHT // 2) == point
#             for point in trail_points
#         )

#         if not collides_with_trail:
#             oval_x = new_oval_x
#             oval_y = new_oval_y

#     # Add the current oval position to the trail points
#     trail_points.append((oval_x + DIAMOND_WIDTH // 2, oval_y + DIAMOND_HEIGHT // 2))

#     # Blit the background image
#     screen.blit(background_image, (0, 0))

#     # Draw the black border around the window
#     pygame.draw.rect(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT), BORDER_THICKNESS)

#     # Calculate the angle of rotation based on the movement direction
#     if current_direction == pygame.K_LEFT:
#         rotation_angle = 0  # No rotation for left movement
#     elif current_direction == pygame.K_RIGHT:
#         rotation_angle = math.pi  # 180 degrees for right movement
#     elif current_direction == pygame.K_UP:
#         rotation_angle = -math.pi / 2  # -90 degrees for upward movement
#     elif current_direction == pygame.K_DOWN:
#         rotation_angle = math.pi / 2  # 90 degrees for downward movement
#     else:
#         rotation_angle = 0  # No rotation for no movement

#     half_oval_width = DIAMOND_WIDTH // 2
#     half_oval_height = DIAMOND_HEIGHT // 2

#     # Calculate rotated vertices for the split oval
#     left_half_vertices = [
#         (oval_x, oval_y + half_oval_height),
#         (oval_x + half_oval_width, oval_y),
#         (oval_x + half_oval_width, oval_y + DIAMOND_HEIGHT)
#     ]

#     right_half_vertices = [
#         (oval_x + half_oval_width, oval_y),
#         (oval_x + DIAMOND_WIDTH, oval_y + half_oval_height),
#         (oval_x + half_oval_width, oval_y + DIAMOND_HEIGHT)
#     ]

#     rotated_left_vertices = [
#         (
#             oval_x + half_oval_width + math.cos(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#             - math.sin(rotation_angle) * (vertex[1] - oval_y - half_oval_height),
#             oval_y + half_oval_height + math.sin(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#             + math.cos(rotation_angle) * (vertex[1] - oval_y - half_oval_height)
#         )
#         for vertex in left_half_vertices
#     ]

#     rotated_right_vertices = [
#         (
#             oval_x + half_oval_width + math.cos(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#             - math.sin(rotation_angle) * (vertex[1] - oval_y - half_oval_height),
#             oval_y + half_oval_height + math.sin(rotation_angle) * (vertex[0] - oval_x - half_oval_width)
#             + math.cos(rotation_angle) * (vertex[1] - oval_y - half_oval_height)
#         )
#         for vertex in right_half_vertices
#     ]

#     pygame.draw.polygon(screen, RED, rotated_left_vertices)  # Red left half
#     pygame.draw.polygon(screen, GREEN, rotated_right_vertices)  # Green right half

#     # Draw the green trail onto the screen
#     if len(trail_points) > 1:
#         pygame.draw.lines(screen, GREEN, False, trail_points, 2)  # Draw a solid green trail line

#     # Update the display
#     pygame.display.update()

# # Clean up
# pygame.mixer.music.stop()  # Stop the music
# pygame.quit()
# sys.exit()