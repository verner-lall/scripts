#!/usr/bin/env python2.7
import sys
import subprocess

if (len(sys.argv) != 2):
	print("set-brightness (int 0-100)")
	exit()
brightness = int(sys.argv[1])
if (brightness > 100 or brightness < 0):
	print("set-brightness (int 0-100)")
	exit()

detectResult = subprocess.check_output(["sudo", "ddcutil", "detect"])

isDisplay = False
displays = []
for line in detectResult.splitlines():
    if line.strip().startswith('Display'):
        isDisplay = True
        continue
    if isDisplay:
        if line.strip().startswith('I2C'):
            displays.append(line.strip().split('i2c-')[-1])
            isDisplay = False

for i in displays:
    subprocess.call(["sudo", "ddcutil", "setvcp", "10", sys.argv[1], "--bus", str(i)])
