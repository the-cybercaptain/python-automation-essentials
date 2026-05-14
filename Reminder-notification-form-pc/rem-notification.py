from winotify import Notification, audio 
import time

while True:
    toast = Notification(app_id = "IMPORTANT", title ="Message", msg ="Please drink water", duration ="short", icon = "C:\\Users\\Hackstar\\Downloads\\download.png")

    toast.set_audio(audio.LoopingCall10, loop = False)

    toast.show()
    time.sleep(10)
