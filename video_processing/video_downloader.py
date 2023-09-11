
from pytube import YouTube
import argparse
import os

# Argument parser for command-line options
parser = argparse.ArgumentParser(description='YouTube Video Downloader')
parser.add_argument('--url', type=str, default='https://www.youtube.com/watch?v=3r7d4qhKCp8', help='YouTube video URL')
parser.add_argument('--output_path', type=str, default='.', help='Path to save the downloaded video')
args = parser.parse_args()

# Validate output path
if not os.path.exists(args.output_path):
    print("Output path does not exist.")
    exit(1)

def download_youtube_video(url, output_path):
    """
    Download a YouTube video.
    Parameters:
    - url: str
        The URL of the YouTube video to download.
    - output_path: str
        The directory where the downloaded video will be saved.
    Returns:
    None
    """
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)
        print("Download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Main execution starts here
    download_youtube_video(args.url, args.output_path)
