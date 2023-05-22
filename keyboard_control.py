from djitellopy import Tello
import pygame

pygame.init()
pygame.display.set_caption("Управление")
screen = pygame.display.set_mode([960, 720])
SPEED = 100

drone = Tello()
drone.connect()

left_right_velocity = 0
for_back_velocity = 0
up_down_velocity = 0
yaw_velocity = 0

fly = True
takeoff = False
f1 = pygame.font.Font(None, 36)

while fly:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                fly = False
            elif event.key == pygame.K_l:
                if takeoff:
                    takeoff = False
                    drone.land()
            elif event.key == pygame.K_t:
                if not takeoff:
                    takeoff = True
                    drone.takeoff()
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
                    yaw_velocity = -SPEED
                if event.key == pygame.K_d:
                    yaw_velocity = SPEED

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

    battary = f1.render(f'Заряд батареи: {drone.get_battery()}%', True, (180, 0, 0))
    tof = f1.render(f'Высота до земли: {drone.get_distance_tof()} см.', True, (180, 0, 0))
    barometer = f1.render(f'Давление воздуха: {drone.get_barometer()}', True, (180, 0, 0))
    time = f1.render(f'Общее время полёта: {drone.get_flight_time()} сек', True, (180, 0, 0))
    temp = f1.render(f'Температура: {int((drone.get_temperature() - 32) / 1.8)}°C', True, (180, 0, 0))

    screen.blit(battary, (10, 50))
    screen.blit(tof, (10, 100))
    screen.blit(barometer, (10, 150))
    screen.blit(time, (10, 200))
    screen.blit(temp, (10, 250))

    pygame.display.update()

if takeoff:
    drone.land()
drone.end()
