import os
import csv
import datetime
from rplidar import RPLidar


# Initialize the RPLIDAR A1 sensor
lidar = RPLidar('/dev/ttyUSB0')
b=[]
for i in range(0,361):
    b.append(i)

try:
    # Start scanning and print scan data
    folder_path = 'ScanData'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Get current date and time for the file name
    current_time = datetime.datetime.now()
    file_name = f"{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(b)
        for scan in lidar.iter_scans():
                a=[]
                print("hi")
                for i in range (1,361):
                    if len(a)<=360:
                        a.append(-1)
                
                for (_, angle, distance) in scan:
                    # Convert angle to degrees
                    angle_degrees = angle
                    # Convert distance to meters
                    distance_meters = distance / 1000.0  # RPLIDAR A1 reports distance in millimeters

                    # Print angle and distance
                    #print(f"Angle: {angle_degrees} degrees, Distance: {distance_meters} meters")
                    a[int(angle_degrees)] = round(angle_degrees,2)
                    print(int(angle_degrees))
                    writer.writerow(a)
                    #a=[]
                

except KeyboardInterrupt:
    print("Stopping the program...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Stop scanning and disconnect from the lidar
    lidar.stop()
    lidar.disconnect()
    print("Lidar motor stopped and disconnected.")
