import sys
import os
import time

from Xlib import X, XK, display, protocol
from Xlib.ext import record

local_dpy = display.Display()
recording_display = display.Display()

#Save these values so that programs don't need to import x
KeyRelease = X.KeyRelease
KeyPress = X.KeyPress

#
# Returns if all the requirements for capturing the keyboard is present.
#
def supportsRecording():
    return recording_display.has_extension("RECORD")

#
# Starts capturing keyboard events and propergates them to a callback
#
def createRecordingContext(callback):
    recArgs = [
        {
            'core_requests': (0, 0),
            'core_replies': (0, 0),
            'ext_requests': (0, 0, 0, 0),
            'ext_replies': (0, 0, 0, 0),
            'delivered_events': (0, 0),
            'device_events': (X.KeyPress, X.MotionNotify),
            'errors': (0, 0),
            'client_started': False,
            'client_died': False,
        }
    ]

    # Create a recording context; we only want key and mouse events (not
    # preocessed)
    context = recording_display.record_create_context(0, [record.AllClients], recArgs)

    recording_display.record_enable_context(context, callback)
    recording_display.record_free_context(context)

#
# Reads the binary keycodes and returns readable ones
#
def parseKeystroke(data):
    eventField = protocol.rq.EventField(None)
    disp = recording_display.display
    return eventField.parse_binary_value(data, disp, None, None)

def send_key(keycode, kind):
    #If a list of keycodes is passed, just call this function for each keycode.
    if type(keycode) is list:
        for char in keycode:
            send_key(char, kind)
        return

    window = local_dpy.get_input_focus()._data["focus"]

    if(kind == X.KeyPress):
        event_to_send = protocol.event.KeyPress(
            time=int(time.time()),
            root=local_dpy.screen().root,
            window=window,
            same_screen=0, child=X.NONE,
            root_x=0, root_y=0, event_x=0, event_y=0,
            state=16,
            detail=keycode
        )
    elif(kind == X.KeyRelease):
        event_to_send = protocol.event.KeyRelease(
            time=int(time.time()),
            root=local_dpy.screen().root,
            window=window,
            same_screen=0, child=X.NONE,
            root_x=0, root_y=0, event_x=0, event_y=0,
            state=16,
            detail=keycode
        )
    else:
        print("Invalid event type. Cancelling keypress")
        return

    window.send_event(event_to_send, propagate=True)

    local_dpy.flush()
    time.sleep(0.01)

def isValidEvent(reply):
    if reply.client_swapped or (reply.category != record.FromServer):
        return False
    if not len(reply.data) or ord(str(reply.data[0])) < 2:  # not an event
        return False

    return True

def getKeyStringFromKeySym(keysym):
    for name in dir(XK):
        if name[:3] == "XK_" and getattr(XK, name) == keysym:
            return name[3:]
    return "[%d]" % keysym

def getKeyStringFromCode(keyCode):
    keysym = local_dpy.keycode_to_keysym(keyCode, 0)
    return getKeyStringFromKeySym(keysym)
