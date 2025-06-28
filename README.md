# Player Tracking with YOLOv11

This project demonstrates how to track football players in a video using a YOLOv11 model (hypothetical) for object detection and DeepSORT for object tracking. The goal is to maintain consistent identities for players even as they move in and out of the camera frame.

## Features
- Player detection using YOLOv11 (hypothetical, similar interface to YOLOv8 from Ultralytics)
- Real-time tracking with DeepSORT
- Identity re-assignment upon player re-entry
- Visualization of tracking results on video frames

## Requirements
Install the necessary Python libraries using pip:

```bash
pip install ultralytics supervision ```

## Usage

```bash
python main.py ```

Make sure to place your input video as video.mp4 and your model weights as best.pt in the same directory, or update the paths accordingly in the script.

## Notes
-This example assumes a YOLOv11 model interface similar to YOLOv8. You may need to modify the code if you use an actual model.

## Licenses
This project is for educational and for evaluation purpose.
