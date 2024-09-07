import cv2
import numpy as np

def get_direction_index(dx, dy):
    # 8-directional chain code directions
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    # Normalize (dx, dy) to unit length
    magnitude = np.sqrt(dx**2 + dy**2)
    if magnitude == 0:
        return None

    dx /= magnitude
    dy /= magnitude

    # Find the closest direction
    min_dist = float('inf')
    closest_index = None
    for i, (dir_x, dir_y) in enumerate(directions):
        # Normalize direction
        dir_mag = np.sqrt(dir_x**2 + dir_y**2)
        dir_x /= dir_mag
        dir_y /= dir_mag

        # Calculate distance between vectors
        dist = np.sqrt((dx - dir_x)**2 + (dy - dir_y)**2)
        if dist < min_dist:
            min_dist = dist
            closest_index = i

    return closest_index

def calculate_chain_code(contour):
    chain_code = []
    start_point = tuple(contour[0][0])
    prev_point = start_point

    for i in range(1, len(contour)):
        current_point = tuple(contour[i][0])
        dx = current_point[0] - prev_point[0]
        dy = current_point[1] - prev_point[1]

        direction_index = get_direction_index(dx, dy)
        if direction_index is not None:
            chain_code.append(direction_index)
        else:
            # Handle case where direction could not be matched
            chain_code.append(-1)  # Use -1 to denote undefined direction

        prev_point = current_point

    return chain_code

# Load image and find contours
image = cv2.imread('shape.png', cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Find the most prominent contour based on the area
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Calculate and print chain code for the most prominent contour
    chain_code = calculate_chain_code(largest_contour)
    print("Chain Code for the most prominent contour:", np.array(chain_code))  # Print chain code as array
else:
    print("No contours found in the image.")
