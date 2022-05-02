from pytube.__main__ import YouTube as yt
link = yt('https://youtube.com/shorts/05n5WqURJaw?feature=share')
print(link.streams)
