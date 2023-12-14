from pytube import YouTube

class YouTubeDownloader:
    def __init__(self):
        self.link = None
        self.data_resolutions = {0: "high", 1: "low"}

    def download_audio(self, resolution, link=None):
        self.link = link if link else self.link
        youtube_object = YouTube(self.link)
        youtube_object = youtube_object.streams.get_audio_only()
        try:
            youtube_object.download()
        except:
            print("An error has occurred")
        print("Download is completed successfully")

    def download_video(self, resolution, link=None):
        self.link = link if link else self.link
        youtube_object = YouTube(self.link)
        resolution = self.data_resolutions[int(resolution)]
        match resolution:
            case "high": youtube_object = youtube_object.streams.get_highest_resolution()
            case "medium": youtube_object = youtube_object.streams.get_lowest_resolution()
            case "low": youtube_object.streams.get_lowest_resolution()
        try:
            media_path = "./../../media/" if __name__ == "__main__" else "./media/"
            youtube_object.download(output_path=media_path)
            print("Download is completed successfully")
        except:
            print("An error has occurred")

    def ask_resolution(self, link):
        data_resolutions = {}
        self.link = link
        youtube_object = YouTube(link)
        data = youtube_object.streaming_data['formats']
        for item in range(0, len(data)):
            data_resolutions[item] = data[item]['qualityLabel']
        self.data_resolutions = data_resolutions
        self.data_resolutions = {0: "high", 1: "low"}
        return self.data_resolutions

# link = input("Enter the YouTube video URL: ")
if __name__ == "__main__":
    ytd = YouTubeDownloader()
    resolutions = ytd.ask_resolution('https://www.youtube.com/watch?v=uVWhzNkw3Cg')
    print(resolutions)
    resolution = input("choose by number")
    ytd.download_video(resolution=resolution)