# to use pyinstaller, first uninstall enum34 with "pip uninstall -y enum34"

# packages to control audio ↓↓
from __future__ import print_function
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import subprocess
import win32api
# packages to control audio ↑↑

# default libraries
import time
import socket
import json
import os

from pynput.keyboard import Key, Controller
from pprint import pp, pprint
import requests
from requests.sessions import PreparedRequest, default_headers
import webbrowser as wb

########################## configuration file ##########################

configPath = "config.json"

# default configurations
config = {
    "id": 0,
    "lastConnDate": "",
    "serverpage": "http://192.168.0.101/localvideosynchronizer/web/",
    "ip_default_numb": 0
}

def config_save():
    with open(configPath, 'w') as outfile:
        json.dump(config, outfile)
        
def config_load():
    with open(configPath) as json_file:
        global config
        config_prev = json.load(json_file)

        for k in config:
            if not k in config_prev:
                config_prev[k] = config[k]

        config = config_prev

# create config file if not exists
if not os.path.isfile(configPath):
    config_save()

config_load()

########################################################################


# class to get local ip
class ipClass():
    list = []
    default_numb = 1

    def __init__(self):
        self.update_list()

    def update_list(self):
        self.list = [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)]
        
    def set_default_numb(self, def_numb = 0):
        self.default_numb = def_numb

    def get(self, numb = None):
        if numb is None:
            numb = self.default_numb

        return self.list[numb]

# create ip object
ip = ipClass()
# set the default ip (in case the machine has multiple ips)
ip.set_default_numb(config["ip_default_numb"])


# control volume functions
def vol_set(val):
    val = float(val)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(val, None)

def vol_setIndv(val):
    val = float(val)
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        # if session.Process and session.Process.name() == "vlc.exe":
        volume.SetMasterVolume(val, None)

def vol_setMax():
    vol_set(0)
    
def vol_setMin():
    vol_set(-96)

def vol_setMaxF():
    win32api.SendMessage(-1, 0x319, 0x30292, 0x0a * 0x10000)

def vol_setMinF():
    win32api.SendMessage(-1, 0x319, 0x30292, 0x09 * 0x10000)

def vol_setIndvMax():
    vol_setIndv(1)

def vol_setIndvMin():
    vol_setIndv(0)


############################ server address ############################

def s(page):
    return config["serverpage"]+page

########################### commands handdler ##########################
kb = Controller()

def kd(key):
    kb.press(key)

def ku(key):
    kb.release(key)

def kt(key):
    kb.press(key)
    kb.release(key)

def exec_cmd(cmd):
    numb = cmd['numb']
    opt = json.loads(cmd['opt'])
    print("received command {0} -> {1}".format(numb, str(opt)))

    if numb == "1":
        wb.register('chrome', None)
        wb.open(opt['url'])
    elif numb == "2":
        for c in opt['act']:
            if(c == "k"):
                kt("k")
            elif(c == "f"):
                kt("f")
            elif(c == "b"):
                kt("0")
            elif(c == ">"):
                kt(Key.right)
            elif(c == "<"):
                kt(Key.left)
            elif(c == "e"):
                kt(Key.esc)
    elif numb == "3":
        mode = opt["mode"]
        if mode == "1":
            # set global value (-96 < val < 0)
            vol_set(opt["val"])
        elif mode == "2":
            # set global max
            vol_setMax()
        elif mode == "3":
            # set global min
            vol_setMin()
        elif mode == "4":
            # set global max (force)
            vol_setMaxF()
        elif mode == "5":
            # set global min (force)
            vol_setMinF()
        elif mode == "6":
            # set individual value (0 < val < 1)
            vol_setIndv(opt["val"])
        elif mode == "7":
            # set individual max
            vol_setIndvMax()
        elif mode == "8":
            # set individual min
            vol_setIndvMin()
    elif numb == "4":
        for c in opt['act']:
            if(c == "n"):
                kd(Key.ctrl)
                kt("n")
                ku(Key.ctrl)
            elif(c == "f"):
                kd(Key.alt)
                kt(Key.f4)
                ku(Key.alt)
            elif(c == "t"):
                kd(Key.ctrl)
                kt("t")
                ku(Key.ctrl)
            elif(c == "c"):
                kd(Key.ctrl)
                kt("w")
                ku(Key.ctrl)
            elif(c == ">"):
                kd(Key.ctrl)
                kt(Key.page_down)
                ku(Key.ctrl)
            elif(c == "<"):
                kd(Key.ctrl)
                kt(Key.page_up)
                ku(Key.ctrl)
    # elif numb == "5":




######## makes the first connection to the server to get its ID ########

r = requests.get(url = s("firstConnection.php"), params = {
    "ip": ip.get(),
    "id": config["id"],
    "lastConnDate": config["lastConnDate"],
})

if r.status_code != 200:
    raise Exception("error in first connection request: ("+str(r.status_code)+") "+ repr(r.content))

try:
    data = r.json()
except:
    raise Exception("error in first connection request: ("+str(r.status_code)+") "+ repr(r.content))


# update received id and lastConnDate
config["id"] = data['id']
config["lastConnDate"] = data['date']
config_save()

############################### main loop ###############################

while(True):
    r2 = requests.get(url = s("getnewcmds.php"), params = {"id": config["id"]})

    if r2.status_code != 200:
        raise Exception("error in getnewcmds request: ("+str(r2.status_code)+") "+ repr(r2.content))

    try:
        data = r2.json()
    except:
        raise Exception("error in getnewcmds request: ("+str(r2.status_code)+") "+ repr(r2.content))

    for cmd in data:
        try:
            exec_cmd(cmd)
        except ValueError:
            print("Got errer"+str(ValueError))

    time.sleep(0.05)

#########################################################################