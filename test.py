from djitellopy import Tello

drone = Tello()
drone.connect()  # подключение
print(drone.get_battery())  # вывод на экран заряда батареи
print(drone.get_distance_tof())  # дистанция до пола
drone.takeoff()  # взлёт

drone.move_forward(100)  # вперёд
drone.move_back(100)  # назад
drone.move_left(100)  # влево
drone.move_right(100)  # вправо

drone.move_up(100)  # вверх
drone.move_down(100)  # вниз

drone.rotate_clockwise(90)  # по часовой стрелке
drone.rotate_counter_clockwise(90)  # против часовой стрелки

drone.land()  # посадка
drone.end()  # отключение
