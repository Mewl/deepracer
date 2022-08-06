import math

def reward_function(params):

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    is_left = params['is_left_of_center']
    
    # Lowest reward
    low_reward = 1e-3
    
    # Yeeting off track is bad
    if not all_wheels_on_track:
        return low_reward;

    # Initialize the reward with typical value
    reward = 1.0
    
    # Left lane is good
    if is_left:
        reward += 1.0;

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    
    # Penalize the reward if the difference is too large
    if direction_diff > 15.0:
        reward *= 0.25
    elif direction_diff > 10.0:
        reward *= 0.5
    elif direction_diff > 5.0:
        reward *= 0.75
    
    return float(reward)