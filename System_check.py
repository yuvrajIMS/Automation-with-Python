#!/usr/bin/env python3
import shutil	 # install stutil using -> "pip3 install pytest-shutil"
import psutil	 # install psutil using -> "pip3 install psutil"
import requests	 # install requests using -> "pip3 install requests"
import socket	 # Already present in standard library. 
import platform
import os
import subprocess
import cpuinfo	# install requests using -> "pip install py-cpuinfo"
import re
import uuid
from datetime import datetime


print("Python Path						: "+ shutil.which("python"))
print('Python version					:', platform.python_version())

print("")

print("Current directory				:", os.getcwd())
print("OS name 						:", os.name)

print("")

print('Systems Name					:', platform.node())
print('Operating System				:', platform.system())
print('Platform processor				:', platform.platform())
print(f"Processor						: {cpuinfo.get_cpu_info()['brand_raw']}")
print("")

boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Booted Since					: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
print("")

print(f"Ip-Address						: {socket.gethostbyname(socket.gethostname())}")
print(f"Mac-Address						: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")

print("")

def check_cpu_usage():
	cputh = psutil.cpu_count()
	cpuco = psutil.cpu_count(logical=False)
	print("")
	print("CPU Speed 						: " + str(psutil.cpu_freq()))	
	print("CPU Threads						: " + str(cputh))
	print("CPU Physical cores				: " + str(cpuco))
	print("")
	print("Wait 1 Second...")
	print("")
	for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
		print(f"Core {i}							: {percentage}%")
	print(f"Total CPU Usage					: {psutil.cpu_percent()}%")
	print("Interrupts  since Boot			: " + str(psutil.cpu_stats().interrupts))
	print("Soft Interrupts  since Boot		: " + str(psutil.cpu_stats().soft_interrupts))
	print("")
	return psutil.cpu_percent() < 75


def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	fs = du.free*(10**-9)
	us = du.used*(10**-9)
	free = (us/(us+fs)*100)
	print("Total Hard Drive Space   		: {:.3f} ".format(fs+us) + "GB")
	print("FREE space in drive 			: {:.3f} ".format(fs) + "GB")
	print("USED space in drive 			: {:.3f} ".format(us) + "GB")
	print("% of space occupied 			: {:.3f} ".format(free) + "%")
	print("")
	return free > 20


def check_memory_usage():
	tm = round(psutil.virtual_memory().total*(10**-9),3)
	um = round(psutil.virtual_memory().used*(10**-9),3)
	am = round(psutil.virtual_memory().available*(10**-9),3)
	acm = round(psutil.virtual_memory().active*(10**-9),3)
	fm = round(psutil.virtual_memory().free*(10**-9),3)
	
	msid = round(psutil.swap_memory().sin*(10**-9),3)
	msod = round(psutil.swap_memory().sout*(10**-9),3)

	print("Total Memory					: " + str(tm) + " GB")
	print("Used Memory						: " + str(um) + " GB")
	print("Available Memory				: " + str(am) + " GB")
	print("Active Memory					: " + str(acm) + " GB")
	print("Free Memory						: " + str(fm) + " GB")
	print("Memory swapped in disk 	 		: " + str(msid) + " GB")
	print("Memory swapped from disk 	 	: " + str(msod) + " GB")
	print("")

	return psutil.virtual_memory()

def check_net():
	
	nds = round(psutil.net_io_counters().bytes_sent*(10**-9),3)
	ndr = round(psutil.net_io_counters().bytes_recv*(10**-9),3)
	nps = psutil.net_io_counters().packets_sent
	npr = psutil.net_io_counters().packets_recv
	
	print("Data Sent						: " + str(nds) + " GB")
	print("Data Received					: " + str(ndr) + " GB")
	print("Packets Sent					: " + str(nps))
	print("Packets Received				: " + str(npr))
	print("")
	
	return psutil.net_io_counters()
	
def batt_usage():
	bt = round( ((psutil.sensors_battery().secsleft)/3600),2)
	print("Charging						: " + str(psutil.sensors_battery().power_plugged))
	print("Battery Level					: " + str(psutil.sensors_battery().percent) + " %" )
	print("Charge left for					: " + str(bt) + " Hours")
	print("")
	
	return psutil.sensors_battery()
	
	
if not check_cpu_usage() or not check_disk_usage('/') or not check_memory_usage() or not check_net() or not batt_usage():
	print("ERROR !")
else:
	print("ALL OPERATIONS COMPLETED !")
	
	
	
