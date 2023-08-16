import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Loading Image')
image = pygame.image.load('images/card_symbols.jpg')
# imagerect = image.get_rect()
# imagerect.center = ((800//2,400//2))
while True:
    screen.fill("white")
    # screen.blit(image,imagerect) # using rect object
    screen.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()













#  Image atribution for down the line <a href="https://www.freepik.com/free-vector/playing-card-symbols-sticker-white-background_21849964.htm#query=black%20jack&position=12&from_view=search&track=ais">Image by brgfx</a> on Freepik