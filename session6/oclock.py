# import datetime
# x = datetime.datetime.now()
# print(x)
import datetime
import pyglet

while True:
    hour = int(input("Nhap gio cua ban :"))
    currentTime = datetime.datetime.now().hour
    if currentTime == hour:
        music = pyglet.resource.media('crowd-cheering.wav.mp3', streaming=False )
        music.play()
        print("play music")
        pyglet.app.run()
    else:
        print("Try again")

