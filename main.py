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
