# Sports-Tracker



## Overview

This repository aims to create a tracker for athletes in sports using pose estimation techniques. The pipeline consists of three main parts:



1. **Video Downloading**: Download YouTube videos for processing.

2. **Pose Estimation**: Estimate human poses in each frame of a video using a pre-trained TensorFlow model.

3. **Video Processing**: Annotate the video with the estimated poses and save the result.



## Installation and Setup



1. Clone the repository.

2. Install the required packages: `pip install -r requirements.txt`.

3. Download the pre-trained PoseNet model and place it in the appropriate directory.



## Usage



1. Update the YouTube URL in `video_downloader.py` and run the script to download the video.

2. Update the paths and run `pose_estimation.py` to perform pose estimation.

3. Run `video_processor.py` to process the video and save the result.



## Technical Details



- **TensorFlow** is used for pose estimation.

- **OpenCV** is used for video processing.

- **Pytube** is used for downloading YouTube videos.
