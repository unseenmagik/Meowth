#!/usr/bin/python3

import sys
import os
import subprocess
import argparse

#Launcher for Magik Bot Sheduler

def parse_cli_args():
    parser = argparse.ArgumentParser(description="Magik Bot Launcher - Pokemon Go Bot for Discord")
    parser.add_argument("--start","-s",help="Starts Meowth",action="store_true")
    parser.add_argument("--auto-restart","-r",help="Auto-Restarts Magik Bot in case of a crash.",action="store_true")
    parser.add_argument("--debug","-d",help="Prevents output being sent to Discord DM, as restarting could occur often.",action="store_true")
    return parser.parse_args()

def run_meowth(autorestart):
    interpreter = sys.executable
    if interpreter is None:
        raise RuntimeError("Python could not be found")

    cmd = [interpreter, "meowth", "launcher"]

    while True:
        if args.debug:
            cmd.append("debug")
        try:
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            code = 0
            break
        else:
            if code == 0:
                break
            elif code == 26:
                #standard restart
                print("")
                print("Restarting Magik Bot")
                print("")
                continue
            else:
                if not autorestart:
                    break
                print("")
                print("Restarting Magik Bot from crash")
                print("")

    print("Magik Bot has closed. Exit code: {exit_code}".format(exit_code=code))

args = parse_cli_args()

if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)

    if args.start:
        print("Launching Magik Bot...")
        run_meowth(autorestart=args.auto_restart)
