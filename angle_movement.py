import math

def calculate_new_xy(oldx, oldy, speed, angle_in_radians):
    newx = oldx + (speed*math.cos(angle_in_radians))
    newy = oldy + (speed*math.sin(angle_in_radians))
    return newx, newy