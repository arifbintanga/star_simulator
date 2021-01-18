import nested_function as nf
import cv2

#User defines the initial attitude
ra = float(input("Input initial right ascension:\n"))
de = float(input("Input initial declination:\n"))
roll = float(input("Input initial roll:\n"))

#Angular rate prompt
print("Input direction:")
print("1. +X\n2. -X\n3. +Y\n4. -Y\n5. +Z\n6. -Z")
direction_sensor = input()
omega = float(input("Input angular rate in degrees: "))

#Frames per second and duration default values
fps = 15.0
duration = 30

#Creating images
images = []
angle_increment = omega/fps
total_frames = int(fps*duration)
if direction_sensor.lower()[-1] == "x" or direction_sensor == "1" or direction_sensor == "2":
    ra_list = [ra]
    if direction_sensor[0] == "-" or direction_sensor == "2":
        angle_increment = - angle_increment
    for i in range(total_frames):
        ra_append = round(ra_list[-1] + angle_increment,3)
        ra_list.append(ra_append)
    
    for ra_step in ra_list:
        images.append(nf.create_star_image(ra_step,de,roll))

elif direction_sensor.lower() == "y":
    de_list = [de]
    for i in range(total_frames):
        de_append = round(de_list[-1] + angle_increment,3)
        de_list.append(de_append)
    
    for de_step in de_list:
        images.append(nf.create_star_image(ra,de_step,roll))

elif direction_sensor.lower() == "z":
    roll_list = [roll]
    for i in range(total_frames):
        roll_append = round(roll_list[-1] + angle_increment,3)
        roll_list.append(roll_append)
    
    for roll_step in roll_list:
        images.append(nf.create_star_image(ra,de,roll_step))

width,height = images[0].shape
out = cv2.VideoWriter('sample_tracking_videos/project.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, (height,width),False)

for i in range(len(images)):
    out.write(images[i])

out.release()