
import os
import logging

def validate_paths(paths):
    """Validate that the specified paths exist."""
    for path in paths:
        if not os.path.exists(path):
            logging.error(f"{path} does not exist.")
            exit(1)
