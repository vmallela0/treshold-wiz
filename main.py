from __future__ import print_function
import tkinter as tk
import cv2 as cv
import numpy as np
import argparse
import time

# selecting the colorspace 
clrspace = []
OptionList = [
"SELECT A COLORSPACE",
"HSV",
"LAB",
"RGB",  
"BGR",
"HSL", 
"YUV"
] 

app = tk.Tk()
app.geometry('300x400')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def close_window():
    print(variable.get())
    clrspace.append(variable.get())
    time.sleep(1)
    app.destroy()

button = tk.Button(text = "ENTER", command = close_window)
button.pack()
def callback(*args):
    labelTest.configure(text="The selected colorspace is {}".format(variable.get()))

global MODE
variable.trace("w", callback)

app.mainloop()

print(clrspace) # 0 = hsv, 1 = lab, 2 = cmyk, 3 = rgb
MODE = clrspace[0]

# threshold settings
max_value = 255
max_value_H = 360//2
bound11 = 0
bound21 = 0
bound31 = 0
bound12 = max_value_H
bound22 = max_value
bound32 = max_value
bound41 = 0
bound42 = 4

window_capture_name = 'Unfiltered video'
window_detection_name = 'Treshold Slider'
clr1 = MODE[0]
clr2 = MODE[1]
clr3 = MODE[2]



bound11_name = 'Low ' + clr1 
bound21_name = 'Low ' + clr2
bound31_name = 'Low ' + clr3
bound12_name = 'High ' + clr1
bound22_name = 'High ' + clr2
bound32_name = 'High ' + clr3


def clrSetter(MODE):
    global clr1
    global clr2
    global clr3
    if MODE == 'HSV':
        clr1 = 'H'
        clr2 = 'S'
        clr3 = 'V'
    elif MODE == 'LAB':
        clr1 = 'L'
        clr2 = 'A'
        clr3 = 'B'
    elif MODE == 'RGB':
        clr1 = 'R'
        clr2 = 'G'
        clr3 = 'B'
    elif MODE == 'CYMK': # FIX LATER
        clr1 = 'R'
        clr2 = 'G'
        clr3 = 'B'
    bound11_name = 'Low ' + clr1 
    bound21_name = 'Low ' + clr2
    bound31_name = 'Low ' + clr3
    bound12_name = 'High ' + clr1
    bound22_name = 'High ' + clr2
    bound32_name = 'High ' + clr3
    
def lowTreshBar1(val):
    global bound11
    global bound12
    bound11 = val
    bound11 = min(bound12-1, bound11)
    cv.setTrackbarPos(bound11_name, window_detection_name, bound11)
def highTreshBar1(val):
    global bound11
    global bound12
    bound12 = val
    bound12 = max(bound12, bound11+1)
    cv.setTrackbarPos(bound12_name, window_detection_name, bound12)
def lowTreshBar2(val):
    global bound21
    global bound22
    bound21 = val
    bound21 = min(bound22-1, bound21)
    cv.setTrackbarPos(bound21_name, window_detection_name, bound21)
def highTreshBar2(val):
    global bound21
    global bound22
    bound22 = val
    bound22 = max(bound22, bound21+1)
    cv.setTrackbarPos(bound22_name, window_detection_name, bound22)
def lowTreshBar3(val):
    global bound31
    global bound32
    bound31 = val     
    bound31 = min(bound32-1, bound31)
    cv.setTrackbarPos(bound31_name, window_detection_name, bound31)
def highTreshBar3(val):
    global bound31
    global bound32
    bound32 = val
    bound32 = max(bound32, bound31+1)
    cv.setTrackbarPos(bound32_name, window_detection_name, bound32)
    
def HSVThreshold(l1, l2, l3, u1, u2, u3):
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (l1, l2, l3), (u1, u2, u3))
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)
    cv.putText()
    
def RGBThreshold(l1, l2, l3, u1, u2, u3):
    frame_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame_threshold = cv.inRange(frame_RGB, (l1, l2, l3), (u1, u2, u3))
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)

def LABThreshold(l1, l2, l3, u1, u2, u3):
    frame_LAB = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    frame_threshold = cv.inRange(frame_LAB, (l1, l2, l3), (u1, u2, u3))
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)

def BGRThreshold(l1, l2, l3, u1, u2, u3):
    frame_BGR = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    frame_threshold = cv.inRange(frame_BGR, (l1, l2, l3), (u1, u2, u3))
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)
    
def HSLThreshold(l1, l2, l3, u1, u2, u3):
    frame_HLS = cv.cvtColor(frame, cv.COLOR_BGR2HLS)
    frame_threshold = cv.inRange(frame_HLS, (l1, l2, l3), (u1, u2, u3))
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)

def YUVThreshold(l1, l2, l3, u1, u2, u3):
    frame_YUV = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
    frame_threshold = cv.inRange(frame_YUV, (l1, l2, l3), (u1, u2, u3))
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)
    
def modeManager(MODE):
    if MODE == 'HSV':
        HSVThreshold(bound11, bound21, bound31,bound12, bound22, bound32)
    elif MODE == 'LAB':
        LABThreshold(bound11, bound21, bound31,bound12, bound22, bound32)
    elif MODE == 'RGB':
        RGBThreshold(bound11, bound21, bound31,bound12, bound22, bound32)
    elif MODE == 'BGR':
        RGBThreshold(bound11, bound21, bound31,bound12, bound22, bound32)
    elif MODE == 'HSL':
        HSLThreshold(bound11, bound21, bound31,bound12, bound22, bound32)
    elif MODE == 'YUV':
        YUVThreshold(bound11, bound21, bound31,bound12, bound22, bound32)
parser = argparse.ArgumentParser(description='Tresholding slider for identifying proper tresholds across OpenCV colorspaces')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)


# Dynamic Trackbars 
cv.createTrackbar(bound11_name, window_detection_name , bound11, max_value_H, lowTreshBar1)
cv.createTrackbar(bound12_name, window_detection_name , bound12, max_value_H, highTreshBar1)
cv.createTrackbar(bound21_name, window_detection_name , bound21, max_value, lowTreshBar2)
cv.createTrackbar(bound22_name, window_detection_name , bound22, max_value, highTreshBar2)
cv.createTrackbar(bound31_name, window_detection_name , bound31, max_value, lowTreshBar3)
cv.createTrackbar(bound32_name, window_detection_name , bound32, max_value, highTreshBar3)



while True:
    ret, frame = cap.read()
    clrSetter(MODE)
    modeManager(MODE)
    key = cv.waitKey(30)
    if key == ord('q') or key == 27 or key == ord('Q') or key == 61:
        break
