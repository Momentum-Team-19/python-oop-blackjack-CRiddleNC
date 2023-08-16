import pygame
pygame.init()

window_size = (800, 800)
screen = pygame.display.set_mode((window_size))

pygame.display.set_caption('Loading Image')
image = pygame.image.load('images/card_symbols.jpg')

image_aspect_ratio = image.get_width() / image.get_height()
image_width = 700
image_height = 700

scaled_image = pygame.transform.scale(image, (image_width, image_height))

while True:
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()













#  Image atribution for down the line <a href="https://www.freepik.com/free-vector/playing-card-symbols-sticker-white-background_21849964.htm#query=black%20jack&position=12&from_view=search&track=ais">Image by brgfx</a> on Freepik