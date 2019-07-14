from __future__ import unicode_literals
import youtube_dl
import json
import pyglet


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info("https://www.youtube.com/watch?v=CxMvQkcdPl8", download=True) 

with open('data.json', 'w') as f:
    json.dump(info_dict, f)

# newString = 'I love coding more than anything else'
# with open("testFile.txt", 'a') as out:
#     out.write(newString )

# music = pyglet.resource.media('crowd-cheering.wav.mp3')
# music.play()
# pyglet.app.run()



from pyglet.media import Source, Player, load

player = Player()
source = load('crowd-cheering.wav.mp3')
player.queue(source)
player.play()
while True:
    input('Press any key to exit')
    break






