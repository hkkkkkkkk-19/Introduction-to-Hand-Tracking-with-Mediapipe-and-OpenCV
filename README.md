# Basic Hand Tracking with MediaPipe
Computer vision, hmm… it always felt like a distant concept to me, something intriguing from afar. But here I am, diving in for the first time! I never imagined that tracking something as simple as a hand could bring so much joy. This code demonstrates the fundamentals of using MediaPipe to understand the basics of hand tracking, focusing on camera initialization, frame processing, and the importance of reversing frames for proper display.
## Overview
Objective: Build a clear understanding of hand tracking.
Tools Used: MediaPipe for hand detection.
Approach: Simple implementation to understand the structure of landmarks and camera setup.
## Requirements
- **Python 3.11** ( Turns out MediaPipe and OpenCV libraries are only supported on **Python 3.9 to 3.12** . Initially, I had Python 3.13 on my VS Code, but I quickly learned that this version wasn’t quite compatible. To temporarily run the code, I used the command to specifically execute it with Python 3.11, rather than the higher version present in my environment.
```bash
py -3.11 .qodo\main.py
```
If you have multiple Python versions installed, this command ensures that you’re explicitly using Python 3.11. This is especially helpful if your default python or python3 points to a different version.)
However,to delve deeper into computer vision and take on more projects on CV, I decided to adjust my VS Code environment variables to permanently run using Python 3.11. So, yeah, that was a significant learning checkpoint, and it’s definitely something to keep in mind! )
- MediaPipe library
- OpenCV library
## How to Run
1. Clone this repository.
2. Install the required dependencies using pip install -r requirements.txt.
## Key Features
- Camera Initialization: Sets up the camera and captures frames.
- Frame Reversal: Frames are reversed for a correct mirror effect.
- Exit Mechanism: Press the Q key to exit the camera view.
## Hand Tracking Landmark Structure
This illustration helped me understand the geometry of how everything is tracked using landmarks in MediaPipe:

<img width="922" height="332" alt="2410344" src="https://github.com/user-attachments/assets/bed160dd-9e60-42a7-9970-d72b2c4b6ec6" />
