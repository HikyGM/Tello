from djitellopy import Tello

drone = Tello()
drone.connect()
print(f'Заряд батареи: {drone.get_battery()}%')
drone.takeoff()
normal_height = 120
for i in range(10):
    start_tof = drone.get_distance_tof()
    d_tof = normal_height - start_tof
    if d_tof > 20:
        drone.move_up(abs(d_tof))
    else:
        drone.move_down(abs(d_tof))
    drone.move_forward(20)
    cur_tof = drone.get_distance_tof()
    print(cur_tof)
    if abs(normal_height - cur_tof) > 15:
        drone.flip_forward()
drone.land()
drone.end()