import cv2
import numpy as np
import sys

preamble = 'bbbddd'
threshold = 150

# read video file
if len(sys.argv) != 2:
    print('Error: incorrect arguments')
    print('usage: python3 visible_light_communication.py <file_name>')
    sys.exit()

cap = cv2.VideoCapture(sys.argv[1]) 
if not cap.isOpened():
    sys.exit()
    print("Error: unable to open video file")

# read frame, compute the middle pixel position
ret, frame = cap.read()
mid_wid = int(frame.shape[0] / 2)
mid_hei = int(frame.shape[1] / 2)

# read the intensity of all frames
intensity = []
while cap.isOpened():
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        intensity.append(gray[mid_wid, mid_hei])
        ret, frame = cap.read()
    else:  
        break
cap.release()

# split the string of intensity with the preamble, get the code
all_code = "".join(list(map(lambda x: ('b' if x > threshold else 'd'), intensity)))
code = all_code.split(preamble)[1]

# decode
binary = ""
idx = 0
while idx < len(code):
    if code[idx] == 'd' and code[idx + 1] == 'b':
        binary = binary + '1'
    elif code[idx] == 'b' and code[idx + 1] == 'd':
        binary = binary + '0'
    else:
        print('Error: incorrect code frames')
        sys.exit()
    idx = idx + 2

# convert binary into decimal, print
decimal = 0
for i in binary:
    decimal = decimal * 2 + int(i)
print(decimal)
