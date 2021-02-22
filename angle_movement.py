import math

def calculate_new_xy(oldx, oldy, speed, angle_in_radians):
    newx = oldx + (speed*math.cos(angle_in_radians))
    newy = oldy + (speed*math.sin(angle_in_radians))
    return newx, newy

def find_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = math.atan2(dy,dx)
    return rads

def find_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)