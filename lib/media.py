import os

def volume_up():
    os.system('amixer -q -D pulse sset Master 5%+')

def volume_down():
    os.system('amixer -q -D pulse sset Master 5%-')

def toggle_mute():
    os.system('amixer -q -D pulse set Master 1+ toggle')
