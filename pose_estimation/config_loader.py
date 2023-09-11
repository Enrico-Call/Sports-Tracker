
import json
import argparse
import logging

def load_config():
    """Load configuration from a JSON file."""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("Configuration file not found. Using default settings.")
        return {}

def parse_arguments(description, argument_list):
    """Parse command-line arguments."""
    config = load_config()
    parser = argparse.ArgumentParser(description=description)
    for arg in argument_list:
        parser.add_argument(arg['name'], type=arg['type'], default=config.get(arg['name'][2:], arg['default']), help=arg['help'])
    args = parser.parse_args()
    logging.info(f"Using configuration: {args.__dict__}")
    return args
