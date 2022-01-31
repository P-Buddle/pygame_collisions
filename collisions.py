# square collisions increase speed, boundary collisions decrease
# number bttons add squares
# add button to increase default vel?
# create CIRCLE image to replace squares

import pygame
import sys
import pygame.midi


class Square:
    """class that creates a square that moves at a set velocity, collides with boundaries and other squares"""

    def __init__(self, x, y, width, height, x_vel, y_vel, color, note):
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.collision_tolerance = 46 + self.y_vel + self.x_vel
        self.color = color
        self.note = note
        # other_rect recognisable as collision object by other instances
        self.other_rect = pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self, window):
        """draws square to display"""
        self.other_rect = pygame.Rect(self.x, self.y, self.height, self.width)
        self.shap = pygame.Rect(self.x, self.y, self.height, self.width)
        self.shapee = pygame.draw.rect(window, self.color, self.shap)
        self.move()

    def move(self):
        """moves square per vel values, checks for collisions with boundaries"""
        self.x += self.x_vel
        self.y += self.y_vel

        # boundary collisions
        vel_inc = 1 #decrease
        # check right
        if self.shap.right >= screen_w and self.x_vel > 0:
            self.x_vel *= -1
            player.note_on(self.note, 70, 0)
            if self.x_vel < -2:
                self.x_vel += vel_inc
        # check left
        if self.shap.left <= 190 and self.x_vel < 0:
            self.x_vel *= - 1
            player.note_on(self.note, 70, 0)
            if self.x_vel > 2:
                self.x_vel -= vel_inc
        # check bottom
        if self.shap.bottom >= screen_h and self.y_vel > 0:
            self.y_vel *= - 1
            player.note_on(self.note, 70, 0)
            if self.y_vel < -2:
                self.y_vel += vel_inc
        # check top
        if self.shap.top <= 110 and self.y_vel < 0:
            self.y_vel *= - 1
            player.note_on(self.note, 70, 0)
            if self.y_vel > 2:
                self.y_vel -= vel_inc

    # object collisions

    def collisions(self, collisee):
        """check for collisions with other objects"""
        vel_inc = 1
        # check collision with bottom
        if self.shap.colliderect(collisee):  # check any collision
            if abs(collisee.top - self.shap.bottom) < self.collision_tolerance:
                if self.y_vel > 0:
                    self.y_vel *= -1
                    player.note_on(self.note, 120, 0)
                    bg_fade()
                    # speed up on collision
                    self.y_vel -= vel_inc

            # check collision with top
            if abs(collisee.bottom - self.shap.top) < self.collision_tolerance:
                if self.y_vel < 0:
                    self.y_vel *= -1
                    player.note_on(self.note, 120, 0)
                    bg_fade()
                    self.y_vel += vel_inc

            # check collision with right
            if abs(collisee.left - self.shap.right) < self.collision_tolerance:
                if self.x_vel > 0:
                    self.x_vel *= -1
                    player.note_on(self.note, 120, 0)
                    bg_fade()
                    self.x_vel -= vel_inc

            # check collision with left
            if abs(collisee.right - self.shap.left) < self.collision_tolerance:
                if self.x_vel < 0:
                    self.x_vel *= -1
                    player.note_on(self.note, 120, 0)
                    bg_fade()
                    self.x_vel += vel_inc


def draw_square(squar):
    """class draw func called for all objects in 'squares' list and checks for collisions with other objects in list"""
    squar.draw(screen)
    for i in squares:
        squar.collisions(i.other_rect)


def bg_fade():
    """changes background gradually through shades of dark and light"""
    global n
    global rgb
    if n < 150:
        if rgb < 150:
            n += 1
            rgb += 0.3
        elif rgb == 150:
            n = 150
    elif n == 150:
        if rgb > 50:
            rgb -= 0.3
        elif rgb == 50:
            n -= 150


# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
sq_width = 50
sq_height = 50

# values for bg_change - starting brightness
n = 120
rgb = 120

# midi sound
pygame.midi.init()
player = pygame.midi.Output(0)
# midi instrument select 0 - 127
#84 nice drones
#34 plinky
instrument = 88
player.set_instrument(instrument)

pygame.init()
clock = pygame.time.Clock()

# small window version
# screen_w, screen_h = 1000, 750
# screen = pygame.display.set_mode((screen_w, screen_h))

# fullscreen version
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_w, screen_h = pygame.display.get_surface().get_size()
# display surface bigger than screen?
# compensate width and height
screen_h -= 110
screen_w -= 190

# default vels
square_x_vel = 2
square_y_vel = 2

# Square objects
# self = class(starting points x and y, width and height defaults, velocity (x and y), colour, note)
# is there a way to create function that automatically generates class object with random parameters?

square = Square(0, 0, sq_width, sq_height, square_x_vel, square_y_vel, (red), 57)
square2 = Square(120, 50, sq_width, sq_height, square_x_vel, square_y_vel, (0, 0, 255), 61)
square3 = Square(240, 100, sq_width, sq_height, square_x_vel, square_y_vel, (0, 255, 0), 64)
square4 = Square(360, 150, sq_width, sq_height, square_x_vel, square_y_vel, (255, 255, 0), 52)
square5 = Square(480, 200, sq_width, sq_height, square_x_vel, square_y_vel, (184, 18, 106), 71)
square6 = Square(600, 250, sq_width, sq_height, square_x_vel, square_y_vel, (0, 255, 255), 73)
square7 = Square(720, 300, sq_width, sq_height, square_x_vel, square_y_vel, (255, 130, 80), 68)
square8 = Square(840, 350, sq_width, sq_height, square_x_vel, square_y_vel, (255, 0, 255), 66)
square9 = Square(960, 400, sq_width, sq_height, square_x_vel, square_y_vel, (255, 255, 255), 78)

# list of squares
squarestats = [square, square2, square3, square4, square5, square6, square7, square8, square9]

# empty list
squares = []

# MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # number keys 1 - 9 add square objects to list - and squares from list are drawn

    if keys[pygame.K_1]:
        squares.clear()
        squares.append(square)
        rang = range(1, 9)
        for i in rang:
            squarestats[i].x_vel = 2
            squarestats[i].y_vel = 2
        # print("1")
    if keys[pygame.K_2]:
        squares.clear()
        squares.extend([square, square2])
        rang = range(2, 9)
        for i in rang:
            squarestats[i].x_vel = 2
            squarestats[i].y_vel = 2
        # print("2")
    if keys[pygame.K_3]:
        squares.clear()
        squares.extend([square, square2, square3])
        rang = range(3, 9)
        for i in rang:
            squarestats[i].x_vel = 2
            squarestats[i].y_vel = 2
        # print("3")
    if keys[pygame.K_4]:
        squares.clear()
        squares.extend([square, square2, square3, square4])
        rang = range(4, 9)
        for i in rang:
            squarestats[i].x_vel = 2
            squarestats[i].y_vel = 2
        # print("4")
    if keys[pygame.K_5]:
        squares.clear()
        squares.extend([square, square2, square3, square4, square5])
        rang = range(5, 9)
        for i in rang:
            squarestats[i].x_vel = 2
            squarestats[i].y_vel = 2
        # print("5")
    if keys[pygame.K_6]:
        squares.clear()
        squares.extend([square, square2, square3, square4, square5, square6])
        rang = range(6, 9)
        for i in rang:
            squarestats[i].x_vel = 2
            squarestats[i].y_vel = 2

        # print("6")
    if keys[pygame.K_7]:
        squares.clear()
        squares.extend([square, square2, square3, square4, square5, square6, square7])
        rang = range(7, 9)
        for i in rang:
            squarestats[i].x_vel = 2
            squarestats[i].y_vel = 2
        # print("7")
    if keys[pygame.K_8]:
        squares.clear()
        square9.x_vel = 2
        square9.y_vel = 2
        squares.extend([square, square2, square3, square4, square5, square6, square7, square8])

    if keys[pygame.K_9]:
        squares.clear()
        squares.extend([square, square2, square3, square4, square5, square6, square7, square8, square9])

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        # del player
        # pygame.midi.quit()

    screen.fill((rgb, rgb, rgb))

# call draw_square function per square in squares[]
    for i in squares:
        draw_square(i)

#refresh display every 60ms
    pygame.display.flip()
    clock.tick(60)
