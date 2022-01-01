# 노래 정보 받기
ydl_opts = {'format': 'bestaudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

# 내가 받고 싶은 노래 유튜브 URL
urls=["https://youtube.com/watch?v=1234",
      "https://youtube.com/watch?v=4321",
      "https://youtube.com/watch?v=2351",
      "https://youtube.com/watch?v=1263",
      "https://youtube.com/watch?v=12632"]

mySongs = []
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        title = info['alt_title']
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        mySongs.append(title)

title = list("TROUBLE,(Prod. By Slom)")
joined_title = "".join(title)
print(joined_title, type(joined_title))
