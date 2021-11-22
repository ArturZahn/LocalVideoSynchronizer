from __future__ import print_function
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import subprocess
import win32api
 
def setMasterVolume(val):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(val, None) #0%

def setIndvVolume(val):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        # if session.Process and session.Process.name() == "vlc.exe":
        volume.SetMasterVolume(val, None)
        

# # setIndvVolume(1)
# setMasterVolume(0)
 
# # Control volume
# # volume.SetMasterVolumeLevel(-0.0, None) #100%
# # volume.SetMasterVolumeLevel(-96.0, None) #0%


# the largest volume
win32api.SendMessage(-1, 0x319, 0x30292, 0x0a * 0x10000)

# the volume of minimum
win32api.SendMessage(-1, 0x319, 0x30292, 0x09 * 0x10000)