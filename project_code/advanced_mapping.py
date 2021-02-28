import picar_4wd as fc
import random
import sys
import time
import math
import numpy as np
from math import sin, cos, floor

SIDE = 36
speed = 10
car_position = [math.floor(SIDE / 2), 0]
car_angle = 90
distance_readings = {
          -60: 0,
          -55: 0,
          -50: 0,
          -45: 0,
          -40: 0,
          -35: 0,
          -30: 0,
          -25: 0,
          -20: 0,
          -15: 0,
          -10: 0,
          -5: 0,
          0: 0,
          5: 0,
          10: 0,
          15: 0,
          20: 0,
          25: 0,
          30: 0,
          35: 0,
          40: 0,
          45: 0,
          50: 0,
          55: 0,
          60: 0
        } # { <angle>: <distance in cm> }
map_array = np.zeros((SIDE, SIDE), int) # Initialize a 5 meter by 5 meter map

np.set_printoptions(8, sys.maxsize)

def move_forward():
    fc.forward(speed)
    fc.stop()
    update_car_position(10)


def move_backward():
    fc.backward(speed)
    update_car_position(-10)

def turn_left():
    fc.turn_left()
    update_car_angle(-30)

def turn_right():
    fc.turn_right()
    update_car_angle(30)

def update_car_position(distance):
    car_positon = ((distance * sin(math.radians(car_angle))) + car_position[0], (distance * cos(math.radians(car_angle))) + car_position[1])

def update_car_angle(angle):
    car_angle = car_angle + angle


def get_coord_for_angle_and_distance(angle, distance):
    relative_coords = (distance * sin(math.radians(angle)), distance * cos(math.radians(angle)))
    print("Relative coords")
    print(relative_coords)
    print("Angle")
    print(angle)
    print("Distance")
    print(distance)
    print("\n\n\n------\n\n\n")
    absolute_x = (relative_coords[0] * sin(math.radians(car_angle)) - relative_coords[1] * sin(math.radians(car_angle))) + car_position[0]
    absolute_y = (relative_coords[1] * cos(math.radians(car_angle)) + relative_coords[0] * sin(math.radians(car_angle))) + car_position[1]
    return (absolute_x, absolute_y)
    
def get_distance_readings():
    for key in distance_readings.keys():
        distance_readings[key] = fc.get_distance_at(-key) # Pass the negative key because the servo's conception of the angle is flipped from ours
        if distance_readings[key] != -2:
            absolute_coords = get_coord_for_angle_and_distance(key, distance_readings[key])
            register_obstacle_at_coords(absolute_coords[0], absolute_coords[1])

def convert_coords_to_array_indices(x, y):
    absolute_x = math.floor(x) + math.floor(SIDE / 2)
    absolute_y = int(abs(math.floor(y) - SIDE))
    if absolute_x >= SIDE or absolute_y >= SIDE:
        return None
    return (absolute_x, absolute_y)

def register_obstacle_at_coords(x, y):
    absolute_coords = convert_coords_to_array_indices(x, y)
    if absolute_coords:
        print("Registering an obstacle at these array indices")
        print(absolute_coords)
        map_array[absolute_coords[1]][absolute_coords[0]] = 1 # Use vertical first to get the outside array

def main():
    get_distance_readings()
    print(distance_readings)
    print(map_array)


if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
