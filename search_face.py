import time
import cv2
from djitellopy import Tello
import pygame

drone = Tello()
drone.connect()
drone.streamoff()

drone.streamon()
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

frame = drone.get_frame_read()

pygame.init()
pygame.display.set_caption("Tello video stream")
screen = pygame.display.set_mode([960, 720])
FPS = 120
SPEED = 100
fly = True

left_right_velocity = 0
for_back_velocity = 0
up_down_velocity = 0
yaw_velocity = 0
takeoff = False
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
                    yaw_velocity = SPEED
                if event.key == pygame.K_d:
                    yaw_velocity = -SPEED

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

    img = frame.frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)
    if len(faces) > 0:

        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


        # for value in faces:
        #     x, y = value[:2]
        #     w, h = value[2:]
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    screen.fill([0, 0, 0])
    frame_t = pygame.surfarray.make_surface(img)
    frame_t = pygame.transform.rotate(frame_t, 270)
    screen.blit(frame_t, (0, 0))
    pygame.display.update()

    time.sleep(1 / FPS)
drone.streamoff()
drone.end()
