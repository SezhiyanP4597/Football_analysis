#import all the required libraries
from ultralytics import YOLO
import supervision as sv
import cv2

#import the custom YOLO model
model=YOLO('model/best.pt')

#object detection
#result= model.predict(source="15sec_input_720p.mp4", save=True)
#Tracking
result= model.track(source="input_videos/video.mp4", save=True,persist=True,conf=0.1,tracker="bytetrack.yaml",show=True)