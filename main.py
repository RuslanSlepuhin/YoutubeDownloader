from APPS.Downloader.youtube_downloader import YouTubeDownloader

if __name__ == '__main__':
    
    link = input('Type the link: ')
    ytb = YouTubeDownloader()
    resolution = ytb.ask_resolution(link)
    print(resolution)
    resolution = input("make the choice: ")
    ytb.download_video(resolution)