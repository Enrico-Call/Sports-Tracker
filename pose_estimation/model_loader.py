
import tensorflow as tf
import logging

def load_model(model_type, model_path):
    """Load the PoseNet model."""
    if model_type == 'PoseNet':
        return tf.keras.models.load_model(model_path)
    logging.warning("Invalid model type specified. Using MockModel.")
    return None
