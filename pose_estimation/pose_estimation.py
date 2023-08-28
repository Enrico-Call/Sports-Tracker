import cv2
import numpy as np
import tensorflow as tf
from video_processing.video_processor import process_video

VIDEO_PATH = 'sample_video.mp4'
OUTPUT_PATH = 'output_video.mp4'

# Load PoseNet model
model = tf.keras.models.load_model('path/to/posenet/model')

def estimate_pose(frame):
    input_image = cv2.resize(frame, (224, 224))
    input_image = np.expand_dims(input_image, axis=0)
    predictions = model.predict(input_image)
    keypoints = predictions[0]
    return keypoints

if __name__ == '__main__':
    process_video(VIDEO_PATH, OUTPUT_PATH, estimate_pose)
