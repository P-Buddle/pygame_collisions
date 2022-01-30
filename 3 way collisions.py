import pygame, sys
import pygame.midi

def bouncing_rect():
    global x_vel, y_vel, x2_vel, y2_vel, x3_vel, y3_vel
    collision_tolerance = 20

#moving third
    third.x += x3_vel
    third.y += y3_vel

    # collisions with borders

    # hit right
    if third.right >= screen_w and x3_vel > 0:
        x3_vel *= - 1
        player.note_on(50, 80, 0)
    # hit left
    if third.left <= 0 and x3_vel < 0:
        x3_vel *= - 1
        player.note_on(50, 80, 0)
    # hit bottom
    if third.bottom >= screen_w and y3_vel > 0:
        y3_vel *= - 1
        player.note_on(50, 80, 0)
    # hit top
    if third.top <= 0 and y3_vel < 0:
        y3_vel *= - 1
        player.note_on(50, 80, 0)

    # third collision with moving_rect

    if third.colliderect(moving_rect):  # check any collision
        if abs(moving_rect.top - third.bottom) < collision_tolerance and y3_vel > 0:  # check where collision is
            y3_vel *= -1
            player.note_on(53, 120, 0)

            x3_vel -= 1
            y3_vel += 1

        if abs(moving_rect.bottom - third.top) < collision_tolerance and y3_vel < 0:  # check where collision is
            y3_vel *= -1
            player.note_on(55, 120, 0)

            x3_vel -= 1
            y3_vel += 1

        if abs(moving_rect.left - third.right) < collision_tolerance and x3_vel > 0:  # check where collision is
            x3_vel *= -1
            player.note_on(57, 120, 0)

            y3_vel -= 1
            x3_vel += 1

        if abs(moving_rect.right - third.left) < collision_tolerance and x3_vel < 0:  # check where collision is
            x3_vel *= -1
            player.note_on(59, 120, 0)

            y3_vel -= 1
            x3_vel += 1

    # third collision with other_rect

    if third.colliderect(other_rect):  # check any collision
        if abs(other_rect.top - third.bottom) < collision_tolerance and y3_vel > 0:  # check where collision is
            y3_vel *= -1
            player.note_on(54, 120, 0)

            x3_vel -= 1
            y3_vel += 1

        if abs(other_rect.bottom - third.top) < collision_tolerance and y3_vel < 0:  # check where collision is
            y3_vel *= -1
            player.note_on(58, 120, 0)

            x3_vel -= 1
            y3_vel += 1

        if abs(other_rect.left - third.right) < collision_tolerance and x3_vel > 0:  # check where collision is
            x3_vel *= -1
            player.note_on(62, 120, 0)

            y3_vel -= 1
            x3_vel += 1

        if abs(other_rect.right - third.left) < collision_tolerance and x3_vel < 0:  # check where collision is
            x3_vel *= -1
            player.note_on(66, 120, 0)

            y3_vel -= 1
            x3_vel += 1

    #############################

    #moving moving_rect
    moving_rect.x += x_vel
    moving_rect.y += y_vel

    #collision with screen borders

    if moving_rect.right >= screen_w and x_vel > 0:
        #print("bonk right")
        player.note_on(62, 80, 0)
        x_vel *= -1
    if moving_rect.left <= 0 and x_vel < 0:
        #print("bonk left")
        player.note_on(62, 80, 0)
        x_vel *= -1
    if moving_rect.bottom >= screen_w and y_vel > 0:
        #print("bonk bottom")
        player.note_on(62, 80, 0)
        y_vel *= - 1
    if moving_rect.top <= 0 and y_vel < 0:
        #print("bonk top")
        player.note_on(62, 80, 0)
        y_vel *= - 1

        # collision with other_rect

    if moving_rect.colliderect(other_rect):  # check any collision
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_vel > 0:  # check where collision is
            y_vel *= -1
            player.note_on(64, 120, 0)

            # collisions cause speed changes!
            # should this be dependable on direction!?
            x_vel -= 1
            y_vel += 1

        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_vel < 0:  # check where collision is
            y_vel *= -1
            player.note_on(65, 120, 0)

            x_vel -= 1
            y_vel += 1

        if abs(other_rect.left - moving_rect.right) < collision_tolerance and x_vel > 0:  # check where collision is
            x_vel *= -1
            player.note_on(67, 120, 0)

            y_vel -= 1
            x_vel += 1

        if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_vel < 0:  # check where collision is
            x_vel *= -1
            player.note_on(69, 120, 0)

            y_vel -= 1
            x_vel += 1

        # collision with third

        if moving_rect.colliderect(third):  # check any collision
            if abs(third.top - moving_rect.bottom) < collision_tolerance and y_vel > 0:  # check where collision is
                y_vel *= -1
                player.note_on(62, 120, 0)


                # collisions cause speed changes!
                # should this be dependable on direction!?
                x_vel -= 1
                y_vel += 1

            if abs(third.bottom - moving_rect.top) < collision_tolerance and y_vel < 0:  # check where collision is
                y_vel *= -1
                player.note_on(66, 120, 0)


                x_vel -= 1
                y_vel += 1

            if abs(third.left - moving_rect.right) < collision_tolerance and x_vel > 0:  # check where collision is
                x_vel *= -1
                player.note_on(70, 120, 0)


                y_vel -= 1
                x_vel += 1

            if abs(third.right - moving_rect.left) < collision_tolerance and x_vel < 0:  # check where collision is
                x_vel *= -1
                player.note_on(74, 120, 0)


                y_vel -= 1
                x_vel += 1

##############################################

    # moving other_rect

    other_rect.y += y2_vel
    other_rect.x += x2_vel

    #collisions with borders

#hit right
    if other_rect.right >= screen_w and x2_vel > 0:
        x2_vel *= - 1
        player.note_on(55, 80, 0)
#hit left
    if other_rect.left <= 0 and x2_vel < 0:
        x2_vel *= - 1
        player.note_on(55, 80, 0)
#hit bottom
    if other_rect.bottom >= screen_w and y2_vel > 0:
        y2_vel *= - 1
        player.note_on(55, 80, 0)
#hit top
    if other_rect.top <= 0 and y2_vel < 0:
        y2_vel *= - 1
        player.note_on(55, 80, 0)

    #other_rect collision with moving_rect

    if other_rect.colliderect(moving_rect):   # check any collision
        if abs(moving_rect.top - other_rect.bottom) < collision_tolerance and y2_vel > 0: #check where collision is
            y2_vel *= -1
            player.note_on(55, 120, 0)

            x2_vel -= 1
            y2_vel += 1

        if abs(moving_rect.bottom - other_rect.top) < collision_tolerance and y2_vel < 0:  # check where collision is
            y2_vel *= -1
            player.note_on(58, 120, 0)

            x2_vel -= 1
            y2_vel += 1

        if abs(moving_rect.left - other_rect.right) < collision_tolerance and x2_vel > 0:  # check where collision is
            x2_vel *= -1
            player.note_on(61, 120, 0)

            y2_vel -= 1
            x2_vel += 1

        if abs(moving_rect.right - other_rect.left) < collision_tolerance and x2_vel < 0: #check where collision is
            x2_vel *= -1
            player.note_on(64, 120, 0)

            y2_vel -= 1
            x2_vel += 1

    #other_rect collision with third

    if other_rect.colliderect(third):   # check any collision
        if abs(third.top - other_rect.bottom) < collision_tolerance and y2_vel > 0: #check where collision is
            y2_vel *= -1
            player.note_on(59, 120, 0)

            x2_vel -= 1
            y2_vel += 1

        if abs(third.bottom - other_rect.top) < collision_tolerance and y2_vel < 0:  # check where collision is
            y2_vel *= -1
            player.note_on(63, 120, 0)

            x2_vel -= 1
            y2_vel += 1

        if abs(third.left - other_rect.right) < collision_tolerance and x2_vel > 0:  # check where collision is
            x2_vel *= -1
            player.note_on(67, 120, 0)

            y2_vel -= 1
            x2_vel += 1

        if abs(third.right - other_rect.left) < collision_tolerance and x2_vel < 0: #check where collision is
            x2_vel *= -1
            player.note_on(71, 120, 0)

            y2_vel -= 1
            x2_vel += 1

    #draw shapes in
    pygame.draw.rect(screen, (255, 255, 255), moving_rect)
    pygame.draw.rect(screen, (0, 0, 0), other_rect)
    pygame.draw.rect(screen, (255, 0, 0), third)

pygame.init()

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(100)

clock = pygame.time.Clock()
screen_w, screen_h = 800, 800
screen = pygame.display.set_mode((screen_w, screen_h))

moving_rect = pygame.Rect(350, 350, 100, 100)
x_vel, y_vel = 2, 3

other_rect = pygame.Rect(300, 600, 100, 100)
x2_vel, y2_vel = 3, 2

third = pygame.Rect(600, 300, 100, 100)
x3_vel, y3_vel = 2, 4


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((130, 130, 130))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)

del player
pygame.midi.quit()