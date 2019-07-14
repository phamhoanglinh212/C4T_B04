from youtube_dl import YoutubeDL
import json, pyglet
from pyglet.media import Source, Player, load
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
    'outtmpl':'%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

option = {
    'outtmpl': '%(id)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3', 
        'preferredquality': '192',
    }]
}
list1 = {
    '1':'Show all songs',
    '2':'Show detail a song',
    '3':'Play a song',
    '4':'Search and download songs',
    '5':'Exit',
}



while True:
    for k,v in list1.items():
        print(k,'.',v)
    choose = input("Pick one of a options: ")
    if choose == '1':
        with open('music.json') as json_file:  
            data = json.load(json_file)
        if len(data) == 0:
            print("Song list is empty")
        else:
            # for i in data:
            #     print(i['title'])
            for i in range(len(data)):
                print(i + 1, '.', data[i]['title'])
        print("-"*20)
    elif choose == '2':
        with open('music.json') as json_file:  
            data = json.load(json_file)
        if 'listData' == 0:
            print("Song list is empty")
        else:
            for i in range(len(data)):
                print(i + 1, '.', data[i]['title'])
            # for i in data:
            #     print(i['title'])
            numSong1 = int(input("The number of song you wanna illustrate: ")) - 1
            print(data[numSong1]['webpage_url'])
        print("-"*20)
    elif choose == '3':
        if 'listData' == 0:
            print("Song list is empty")
        else:
            with open('music.json') as json_file:  
                data = json.load(json_file)
            for i in range(len(data)):
                print(i + 1, '.', data[i]['title'])
            numSong2 = int(input("The number of song you wanna play: ")) - 1
            urlMusic = data[numSong2]['title'] + ".mp3"
            player = Player()
            source = load(urlMusic)
            player.queue(source)
            player.play()
            while True:
                choice = input("Play Pause or Stop ? ").lower()
                if choice == "play":
                    player.play()
                if choice == "pause":
                    player.pause()
                elif choice == "stop": 
                    break
            if choice == "stop":
                player.pause()
                pass
        print("-"*20)
# urlMusic = data[numSong]['tiltle'] + ".mp3"
    elif choose == '5':
        break
    elif choose == '4':
        with open('music.json') as json_file:  
            data = json.load(json_file)
        song = input("Enter the song you wanna search: ")
        options = {'default_search': 'ytsearch3'}
        ydl = YoutubeDL(options)
        search_result = ydl.extract_info(song, False)
        for i in range(len(search_result['entries'])):
            print (i +1,'.', search_result['entries'][i]['title'])
        numSong = int(input("The number of song you wanna download: ")) - 1
        urlDowndload = search_result['entries'][numSong]['webpage_url']
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([urlDowndload])
        with YoutubeDL(ydl_opts) as ydl:
            newData = ydl.extract_info(urlDowndload, download=True)
        data.append(newData)
        with open('music.json', 'w') as f:
            json.dump(data, f)
        print("-"*20)
        
        
        
        
