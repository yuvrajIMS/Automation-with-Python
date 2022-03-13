#!/usr/bin/env python3
import shutil	 # install stutil using -> "pip3 install pytest-shutil"
import psutil	 # install psutil using -> "pip3 install psutil"
import requests	 # install requests using -> "pip3 install requests"
import socket	 # Already present in standard library. 

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	fs = du.free*(10**-9)
	us = du.used*(10**-9)
	free = (us/(us+fs)*100)
	print("Total Drive Space   : {:.3f} ".format(fs+us) + "GB")
	print("FREE space in drive : {:.3f} ".format(fs) + "GB")
	print("USED space in drive : {:.3f} ".format(us) + "GB")
	print("% of space occupied : {:.3f} ".format(free) + "%")
	return free > 20

def check_cpu_usage():
	cputh = psutil.cpu_count()
	cpuco = psutil.cpu_count(logical=False)
	usage = psutil.cpu_percent(1)
	print("CPU Speed           : " + str(psutil.cpu_freq()))	
	print("CPU Threads         : " + str(cputh))
	print("CPU Physical cores  : " + str(cpuco))
	print("CPU Usage           : " + str(usage) + "%")
	print("")
	return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
	print("ERROR !")
else:
	print("Everything OK :)")
	


	