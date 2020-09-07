import pygame

pygame.init()

white = (255,255,250)
x = 800#width screen
y = 500#height screen
z = [x,y]

win = pygame.display
win.set_caption('My window')
surface = win.set_mode(z)
python = pygame.image.load('digitech2.png')
window = True
while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False
    surface.fill(white)
    surface.blit(python,(150,150))#up and down the image
    win.update()
pygame.quit()