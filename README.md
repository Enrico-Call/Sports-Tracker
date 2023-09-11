
# Sports Tracker

## Overview
This repository contains code for tracking human poses in sports videos.

## Setup
1. Clone this repository.
2. Install the required packages: `pip install -r requirements.txt`

## Usage
You can run the pose estimation and video processing scripts as follows:

### Pose Estimation
```bash
python pose_estimation/pose_estimation.py --video_path 'path/to/video' --model_path 'path/to/model'
```

### Video Processing
```bash
python video_processing/video_processor.py --input_path 'path/to/input_video' --output_path 'path/to/output_video'
```

## Code Structure
The code has been modularized for better readability and maintainability. Here are the key modules:

### pose_estimation
- `pose_estimation.py`: Main script for pose estimation.
- `config_loader.py`: Loads configuration from a JSON file and command-line arguments.
- `utils.py`: Utility functions like data validation.
- `model_loader.py`: Loads machine learning models for pose estimation.

### video_processing
- `video_processor.py`: Main script for video processing.
- `video_downloader.py`: Utility script for downloading videos (if needed).

## Configuration
You can specify the settings in a `config.json` file. See `config_sample.json` for an example.

## Contributing
1. Fork the repository.
2. Create a new branch for each feature or bugfix.
3. Submit a pull request for review.

## License
See [LICENSE](LICENSE) for details.

