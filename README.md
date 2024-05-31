# YouTube Video Downloader

This script downloads a YouTube video in the highest available resolution among a list of preferred resolutions. If none of the preferred resolutions are available, it defaults to the highest available resolution.

## Prerequisites

- Python 3.x
- `pytube` library

You can install `pytube` using pip:

```sh
pip install pytube
```

## Usage

1. Run the script.
2. Enter the URL of the YouTube video when prompted.
3. The script will attempt to download the video in the highest resolution available among the preferred resolutions (`1080p`, `720p`, `480p`).
4. If none of the preferred resolutions are available, it will download the video in the highest available resolution.

## Code

```python
from pytube import YouTube

# Prompt the user for the YouTube video URL
video_url = input('Video URL : ')

# List of preferred resolutions
preferred_resolutions = ['1080p', '720p', '480p']

print('Starting...')
try:
    yt = YouTube(video_url)  # Create a YouTube object
    video = None
    
    # Try to find the video in the preferred resolutions
    for resolution in preferred_resolutions:
        video = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()
        if video:
            break
    
    # If none of the preferred resolutions are available, fallback to the highest available resolution
    if not video:
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    # Download the selected video stream
    video.download(f"Videos/{yt.author}")
    print('Download complete!')
except Exception as e:
    print('Failed to download the video!')
    print(f'Error: {e}')
```

## Explanation

1. **Imports**:
    - `from pytube import YouTube`: Imports the `YouTube` class from the `pytube` library to interact with YouTube videos.

2. **Input**:
    - `video_url = input('Video URL : ')`: Prompts the user to enter the URL of the YouTube video.

3. **Preferred Resolutions**:
    - `preferred_resolutions = ['1080p', '720p', '480p']`: Defines a list of preferred resolutions in descending order.

4. **Download Process**:
    - The script tries to find and download the video in the highest available resolution from the preferred list.
    - If none of the preferred resolutions are available, it defaults to downloading the video in the highest available resolution.

5. **Error Handling**:
    - The script includes a try-except block to handle any errors that may occur during the download process, printing an error message if the download fails.

## Output

The downloaded video will be saved in a folder named `Videos`, organized by the author's name. The script prints a completion message upon successful download or an error message if the download fails.