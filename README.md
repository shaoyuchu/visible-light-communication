# Visible Light Communication

### Task
Decode **Manchester coding** with:
1. 30 frames per second
2. 1/15 sec per symbol
3. 01 -> 1
4. 10 -> 0
5. preamble 111000 (1/30 sec per symbol)

### Language & Platform
The program is written in python3 and utilizes the OpenCV library.

### Procedure
1.	Read the .mp4 file.
2.	For every frame, get the intensity value of the center pixel.
3.	Test the intensity value with a threshold and decide whether the pixel is bright (b) or dark (d).
4.	Find the string of b/d that is in between a pair of preambles (bbbddd).
5.	Split the string into character pairs. Convert “db” into 1 and “bd” into 0.
6.	Convert the binary integer into decimal.

### Execute
python3 visible_light_communication.py \<filename>
