
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

## Configuration
You can specify the settings in a `config.json` file. See `config_sample.json` for an example.

## Contributing
1. Fork the repository.
2. Create a new branch for each feature or bugfix.
3. Submit a pull request for review.

## License
See [LICENSE](LICENSE) for details.
