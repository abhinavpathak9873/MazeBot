import pygame
import math
from rplidar import RPLidar

pygame.init()

# Constants
LIDAR_RESOLUTION = 360
VISUALIZATION_RESOLUTION = 360

# Function to generate line positions based on the number of lines
def generate_line_positions(number_of_lines):
    angle = 360 / number_of_lines
    lines = []
    for x in range(number_of_lines):
        lines.append([300 * math.cos((x + 1) * angle / 180 * math.pi), 300 * math.sin((x + 1) * angle / 180 * math.pi)])
    return lines

line_positions = generate_line_positions(VISUALIZATION_RESOLUTION)

# Set up the drawing window
screen = pygame.display.set_mode([800, 800])

# Initialize RPLIDAR A1 sensor
lidar = RPLidar('/dev/ttyUSB0')

try:
    running = True
    # Main loop
    for scan in lidar.iter_scans():
        # Check if the user clicked the window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        if not running:
            break

        # Fill the background with white
        screen.fill((250, 250, 250))

        # Process lidar scan data
        for (_, angle, distance) in scan:
            # Convert distance to meters
            distance_meters = distance / 1000.0  # RPLIDAR A1 reports distance in millimeters

            # Determine the position to draw based on angle and distance
            angle_index = int(angle) % LIDAR_RESOLUTION  # Ensure angle index is within range
            if angle_index < VISUALIZATION_RESOLUTION:
                # Calculate the position based on polar to Cartesian coordinates
                x = distance_meters * math.cos(math.radians(angle))
                y = distance_meters * math.sin(math.radians(angle))
                
                # Scale the position for visualization
                x_visual = int(x * 100)  # Adjust scale for visualization
                y_visual = int(y * 100)  # Adjust scale for visualization
                
                # Draw the point at the calculated position
                pygame.draw.circle(screen, (255, 0, 0), (400 + x_visual, 400 + y_visual), 2)

        # Draw lidar center point
        pygame.draw.circle(screen, (0,0,0), (400, 400), 12)

        # Flip the display
        pygame.display.flip()
        #pygame.time.wait(50)  # Adjust delay as needed for visualization speed

finally:
    # Stop scanning and disconnect from the lidar
    lidar.stop()
    lidar.disconnect()
    pygame.quit()
