#!/usr/bin/env python3
import sys
import os
import subprocess
import dbus

from time import time

APP_ID = 'cz.synaptiko'
CLASS = 'Kickterm'
NAME = 'kickterm'

SERVER_CMD = [
    '/usr/lib/gnome-terminal/gnome-terminal-server',
    '--app-id', APP_ID,
    '--class', CLASS,
    '--name', NAME,
]
TERMINAL_CMD = [
    'gnome-terminal',
    '--app-id', APP_ID,
    '--class', CLASS,
    '--name', NAME,
    '--hide-menubar'
]

def runNewTerminal():
    session_bus = dbus.SessionBus()
    if not session_bus.name_has_owner(APP_ID):
        subprocess.Popen(SERVER_CMD)
    timeout = time() + 2
    while not session_bus.name_has_owner(APP_ID) and time() <= timeout:
        pass
    if session_bus.name_has_owner(APP_ID):
        env = os.environ.copy()
        with open(os.devnull, 'wb') as fnull:
            subprocess.Popen(TERMINAL_CMD,
                             stdout=fnull,
                             stderr=fnull,
                             env=env)

def main():
    runNewTerminal()

if __name__ == '__main__':
    main()
