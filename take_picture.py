import cv2
from djitellopy import Tello

drone = Tello()
drone.connect()

drone.streamon()
frame_read = drone.get_frame_read()
drone.takeoff()
drone.move_up(70)
for i in range(4):
    cv2.imwrite(f"picture_{i}.png", frame_read.frame)
    drone.rotate_clockwise(90)
    drone.move_forward(60)
    drone.rotate_counter_clockwise(135)
    cv2.imwrite(f"picture_angle_{i}.png", frame_read.frame)
    drone.rotate_clockwise(45)
    drone.move_forward(60)
    drone.rotate_counter_clockwise(90)
drone.streamoff()
drone.land()
drone.end()