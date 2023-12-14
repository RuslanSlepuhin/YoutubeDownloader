import pafy

url = "https://www.youtube.com/watch?v=uVWhzNkw3Cg"
video = pafy.new(url)
best = video.getbest()
best.download()