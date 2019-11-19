# Author: Michael Le
# Date: 10/21/2019
# Description: Function that determines distance object falls based on gravity

def fall_distance(time):
    """
    Returns a float for distance fallen based on entered float or integer for time.
    Calculates distance of fallen object based on gravity input default of 9.8
    time is in seconds and distance is in meters
    """
    gravity = 9.8
    distance = (1/2)*(gravity)*(time**2)
    print(distance)
    return distance


