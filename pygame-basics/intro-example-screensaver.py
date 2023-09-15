import sys, pygame
pygame.init()

size=width, height = 1080, 900 # if make it square, just traverses diagonal
speed=[1,1] #must be in integers
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("images/ball.jpg")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0] #reverse on sides
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1] #reverses at top

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()