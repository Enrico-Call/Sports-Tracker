from pytube import YouTube

YOUTUBE_URL = 'https://www.youtube.com/watch?v=3r7d4qhKCp8'
OUTPUT_PATH = "."

def download_youtube_video(url, output_path=OUTPUT_PATH):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")

        # Download the video to output_path
        video_stream.download(output_path)

        print("Download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video(YOUTUBE_URL)
