import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Growing Squares")

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
turquiose = (48, 213, 200)


screen.fill(turquiose)

class Square:
    def __init__(self, color, pos, size, width=0):
        

        
        self.color = color
        self.pos = pos
        self.size = size
        self.width = width
        self.screen = screen

    def draw(self):
        
        pygame.draw.rect(self.screen, self.color, (self.pos, self.size, self.size), self.width)

    def grow(self, increment):
        self.size += increment
        self.pos = (self.pos[0] - increment // 2, self.pos[1] - increment // 2)

initial_size = 10
position = (250 - initial_size // 2, 250 - initial_size // 2)  
squares = [Square(blue, position, initial_size)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            new_squares = [
                Square(blue, position, squares[-1].size + 20),
                Square(red, position, squares[-1].size + 40),
                Square(green, position, squares[-1].size + 60),
                Square(yellow, position, squares[-1].size + 80),
            ]
            squares.extend(new_squares)

    screen.fill(turquiose)  
    for square in squares:
        square.draw()
    pygame.display.update()

pygame.quit()
