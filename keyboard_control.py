from djitellopy import Tello
import time
import pygame

pygame.init()
pygame.display.set_caption("Управление")
screen = pygame.display.set_mode([960, 720])
FPS = 120
SPEED = 100

drone = Tello()
drone.connect()
drone.takeoff()
fly = True

left_right_velocity = 0
for_back_velocity = 0
up_down_velocity = 0
yaw_velocity = 0

while fly:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                fly = False

            else:

                if event.key == pygame.K_UP:
                    for_back_velocity = SPEED
                if event.key == pygame.K_DOWN:
                    for_back_velocity = -SPEED

                if event.key == pygame.K_RIGHT:
                    left_right_velocity = SPEED
                if event.key == pygame.K_LEFT:
                    left_right_velocity = -SPEED

                if event.key == pygame.K_w:
                    up_down_velocity = SPEED
                if event.key == pygame.K_s:
                    up_down_velocity = -SPEED

                if event.key == pygame.K_a:
                    yaw_velocity = SPEED
                if event.key == pygame.K_d:
                    yaw_velocity = -SPEED

                if event.key == pygame.K_SPACE:
                    drone.flip_forward()

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                for_back_velocity = 0

            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                left_right_velocity = 0

            if event.key == pygame.K_w or event.key == pygame.K_s:
                up_down_velocity = 0

            if event.key == pygame.K_a or event.key == pygame.K_d:
                yaw_velocity = 0

    drone.send_rc_control(left_right_velocity, for_back_velocity, up_down_velocity, yaw_velocity)

    screen.fill([0, 0, 0])
    pygame.display.update()

    time.sleep(1 / FPS)

drone.land()
drone.end()
