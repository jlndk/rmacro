#!/usr/bin/python
import sys
import os

from lib import keyboard

def main():

    # Check if the extension is present
    if not keyboard.supportsRecording():
        print("Cannot record keyboard. RECORD extension not found")
        sys.exit(1)

    # Start keyboard capturing
    keyboard.createRecordingContext(onGlobalKeypress)

def onGlobalKeypress(reply):
    #We only care about legit keypresses. Therefore ignore everything else
    if not keyboard.isValidEvent(reply):
        return

    # Loop through all keystrokes and handle them one-by-one
    while len(reply.data):
        #But first we need to parse the keycode since it's in a binary format.
        event, reply.data = keyboard.parseKeystroke(reply.data)
        #Then we can handle the event
        handleKeyEvent(event)


def handleKeyEvent(event):
    if event.type == keyboard.KeyRelease:
        clearScreen()
        keyString = keyboard.getKeyStringFromCode(event.detail)

        print "Key '{1}' pressed with keycode '{0}'".format(event.detail, keyString)


def clearScreen():
    os.system("clear")
    print "Press a key to see the keycode."

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        os.system("clear")
        sys.exit(0)
