from pytube import YouTube

def download_video(url, path="./"):
    try:
        
        yt = YouTube(url)

    
        stream = yt.streams.get_highest_resolution()

        print(f"Downloading {yt.title}...")
        stream.download(output_path=path)
        print("Download completed!")

    except Exception as e:
        print(f"Error downloading the video: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)

