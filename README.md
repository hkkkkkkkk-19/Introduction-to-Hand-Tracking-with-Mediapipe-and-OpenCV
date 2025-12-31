# Basic Hand Tracking with MediaPipe
Computer vision, hmm… it always felt like a distant concept to me, something intriguing from afar. But here I am, diving in for the first time! I never imagined that tracking something as simple as a hand could bring so much joy. This code demonstrates the fundamentals of using MediaPipe to understand the basics of hand tracking, focusing on camera initialization, frame processing, and the importance of reversing frames for proper display.
## Overview
Objective: Build a clear understanding of hand tracking.
Tools Used: MediaPipe for hand detection.
Approach: Simple implementation to understand the structure of landmarks and camera setup.
## Requirements
- Python 3.11
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
