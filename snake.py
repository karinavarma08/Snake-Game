import random
import pygame
import sys
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.head_up =pygame.image.load("head_up.png").convert_alpha()
        self.head_down  = pygame.image.load("head_down.png").convert_alpha()
        self.head_left = pygame.image.load("head_left.png").convert_alpha()
        self.head_right = pygame.image.load("head_right.png").convert_alpha()

        self.tail_up = pygame.image.load ("tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load ("tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load ("tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load ("tail_right.png").convert_alpha()

        self.body_tr=  pygame.image.load ("body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load ("body_tl.png").convert_alpha()
        self.body_br = pygame.image.load ("body_br.png").convert_alpha()
        self.body_bl = pygame.image.load ("body_bl.png").convert_alpha()

        self.body_vertical  = pygame.image.load ("body_vertical.png").convert_alpha()
        self.body_horizontal  = pygame.image.load ("body_horizontal.png").convert_alpha()





        self.direction = Vector2 (1, 0)
        self.body = [Vector2 (5, 10), Vector2 (4, 10), Vector2 (3, 10)]
        self.new_block = False

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()




        for index,block in enumerate(self.body):

            snake_rect = pygame.Rect (block.x * cell_size, block.y * cell_size, cell_size,cell_size)  # CREATE A RECTANGLE, DRAW A RECTANGLE


            if index == 0:
                screen.blit(self.head,snake_rect)

            elif index == len(self.body) - 1:
                screen.blit(self.tail,snake_rect)

            else:
                previous_block = self.body[index+1] - block
                next_block = self.body[index-1] - block

                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,snake_rect)

                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,snake_rect)

                else:

                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x ==-1:
                        screen.blit(self.body_tl,snake_rect)

                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,snake_rect)

                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit (self.body_bl, snake_rect)

                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit (self.body_br, snake_rect)


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]

        if head_relation == Vector2 (1,0) : self.head = self.head_left
        elif head_relation == Vector2 (-1, 0): self.head = self.head_right
        elif head_relation == Vector2 (0, 1): self.head = self.head_up
        elif head_relation == Vector2 (0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation =self.body[-2] - self.body[-1]

        if tail_relation == Vector2(1,0) : self.tail= self.tail_left
        elif tail_relation == Vector2 (-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2 (0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2 (0, -1): self.tail = self.tail_down
        


    def move_snake(self):  # method
        if self.new_block == True:
            body_copy = self.body[:]  # copy entire body but remove the last part by slicing
            body_copy.insert (0, body_copy[0] + self.direction)  # created the head at position 0, i.e first element of the previous list.
            self.body = body_copy[:]
            self.new_block =False

        else:
            body_copy = self.body[:-1]  # copy entire body but remove the last part by slicing
            body_copy.insert (0, body_copy[0] + self.direction)  # created the head at position 0, i.e first element of the previous list.
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True



class Fruit:

    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect (self.pos.x * cell_size, self.pos.y * cell_size, cell_size,cell_size)  # CREATE A RECTANGLE, DRAW A RECTANGLE
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect (screen, (100, 100, 255), fruit_rect)

    def randomize(self):
        self.x = random.randint (0, cell_numbers - 2)  # an x and  y position ,
        self.y = random.randint (0, cell_numbers - 2)
        self.pos = Vector2 (self.x, self.y)  # draw a square i.e



class MAIN:

    def __init__(self):
        self.snake = Snake ()
        self.fruit = Fruit ()

    def update(self):
        self.snake.move_snake ()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit ()
        self.snake.draw_snake ()

    def check_collision(self):        #repostion fruit after eaten  #add another block to snake, i.e make it longer
        if self.fruit.pos == self.snake.body[0]:
           self.fruit.randomize()
           self.snake.add_block()


    def check_fail(self):                           #check if snake is outside the screen and hits itself
        if not 0 <= self.snake.body[0].x < cell_numbers:
            self.game_over()

        elif not 0 <= self.snake.body[0].y < cell_numbers:
            self.game_over ()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit ()
        sys.exit ()


pygame.init ()
cell_size = 30
cell_numbers = 20
screen = pygame.display.set_mode ((cell_size * cell_numbers, cell_size * cell_numbers))  # main screen
test_surface = pygame.Surface ((100, 100))  # width and height of a block #inside screen small block
pygame.display.set_caption ("Snake Game")
clock = pygame.time.Clock ()
apple =pygame.image.load("finalapples.jpg")
# fruit = Fruit()
# snake = Snake() #create object of that class

SCREEN_UPDATE = pygame.USEREVENT  # we are creating customized event that could be triggered by creating a timer
pygame.time.set_timer (SCREEN_UPDATE, 150)  # so screen_update trigger is going to run every 190 ms

main = MAIN ()

while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()

        if event.type == SCREEN_UPDATE:
            # snake.move_snake()
            main.update ()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1:
                    main.snake.direction = Vector2 (0, -1)

            if event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1:
                    main.snake.direction = Vector2 (0, 1)

            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = Vector2 (1, 0)

            if event.key == pygame.K_LEFT:
                if main.snake.direction.x !=  1:
                    main.snake.direction = Vector2 (-1, 0)


    screen.fill ((255, 255, 0))  # background color
    # fruit.draw_fruit()
    # snake.draw_snake()
    main.draw_elements ()
    pygame.display.update ()
    clock.tick (60)
