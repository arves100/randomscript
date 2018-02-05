#!/usr/local/bin/python
# Created by Arves100 on 05-02-2018 for rewardmetin2
# Released under MIT license (this shit is licensed o.O)
#

import os

core_list = []
dir_list = []

def make_core(base, folder, name, share):
	# Remove core file
	os.system("rm -rf " + base + "/" + folder + "/" + name)
	
	# Remove shared folders
	os.system("rm -rf " + base + "/" + folder + "/locale")
	os.system("rm -rf " + base + "/" + folder + "/data")
	os.system("rm -rf " + base + "/" + folder + "/package")
	os.system("rm -rf " + base + "/" + folder + "/panama")
	
	# Clean logs
	os.system("rm -rf " + base + "/" + folder + "/log")
	os.system("rm -rf " + base + "/" + folder + "p2p_packet_info.txt")
	os.system("rm -rf " + base + "/" + folder + "packet_info.txt")
	os.system("rm -rf " + base + "/" + folder + "ProfileLog")
	os.system("rm -rf " + base + "/" + folder + "udp_packet_info.txt")
	os.system("rm -rf " + base + "/" + folder + "DEV_LOG.txt")
	os.system("rm -rf " + base + "/" + folder + "*.core")
	os.system("rm -rf " + base + "/" + folder + "syslog")
	os.system("rm -rf " + base + "/" + folder + "syserr")
	os.system("rm -rf " + base + "/" + folder + "stdout")
	
	# Share data links
	os.system("ln -s " + base + "/" + share + "/locale " + base + "/" + folder + "/locale")
	os.system("ln -s " + base + "/" + share + "/data " + base + "/" + folder + "/data")
	os.system("ln -s " + base + "/" + share + "/package " + base + "/" + folder + "/package")
	os.system("ln -s " + base + "/" + share + "/panama " + base + "/" + folder + "/panama")
	
	# Core file
	os.system("ln -s " + base + "/" + share + "/game " + base + "/" + folder + "/" + name)

	# Folder
	os.system("mkdir " + base + "/" + folder + "/log")
	
def make_db(base, folder, share):
	# Remove core file
	os.system("rm -rf " + base + "/" + folder + "/db")
	
	# Clean logs
	os.system("rm -rf " + base + "/" + folder + "/log")
	os.system("rm -rf " + base + "/" + folder + "p2p_packet_info.txt")
	os.system("rm -rf " + base + "/" + folder + "packet_info.txt")
	os.system("rm -rf " + base + "/" + folder + "ProfileLog")
	os.system("rm -rf " + base + "/" + folder + "udp_packet_info.txt")
	os.system("rm -rf " + base + "/" + folder + "DEV_LOG.txt")
	os.system("rm -rf " + base + "/" + folder + "*.core")
	os.system("rm -rf " + base + "/" + folder + "syslog")
	os.system("rm -rf " + base + "/" + folder + "syserr")
	os.system("rm -rf " + base + "/" + folder + "stdout")
	os.system("rm -rf " + base + "/" + folder + "uasge.txt")
	
	# Core file
	os.system("ln -s " + base + "/" + share + "/db " + base + "/" + folder + "/db")

	# Folder
	os.system("mkdir " + base + "/" + folder + "/log")
	
def make_share(base, share, locale):
	os.system("rm -rf " + base + "/" + share + "/data/data")
	os.system("rm -rf " + base + "/quest")
	os.system("rm -rf " + base + "/" + share + "/locale/" + locale + "/quest/qc")
	os.system("rm -rf " + base + "/" + share + "/game")
	os.system("rm -rf " + base + "/" + share + "/db")
	
	os.system("ln -s " + base + "/" + share + "/locale/" + locale + "/quest " + base + "/quest")

def clear_rage50k_files(base, share, locale):
	os.system("rm -rf " + base + "/" + share + "/gamefile")
	os.system("rm -rf " + base + "/" + share + "/logs")
	os.system("rm -rf " + base + "/" + share + "/locale" + locale + "/quest/Connetion_Refused")
	os.system("rm -rf " + base + "/" + share + "/data/*/.svn")
	os.system("rm -rf " + base + "/" + share + "/data/*/.svn")
	os.system("rm -rf " + base + "/log")
	os.system("rm -rf " + base + "/backups")
	
def entry_point():
	print("(Base directory) Input the dir where you have installed your server files without the final slash (example: /usr/home/game)")
	base = raw_input()
	if len(base) < 1:
		print("Please input something!")
		return
	
	print("Input your share directory without the base directory (example: share)")
	share = raw_input()
	if len(share) < 1:
		print("Please input something!")
		return
		
	print("Input your locale name: (example: italy)")
	locale = raw_input()
	if len(locale) < 1:
		print("Please input something!")
		return
		
	print("Do you have Ragemt2 50k and want to clean a part of it? (Yes, No)")
	clean = raw_input()
	
	if clean == "Yes":
		print("Clearing...")
		clear_rage50k_files(base, share, locale)
		
	print("Do automatic channel symlink (only for rage50k files)? (Yes, No)")
	auto = raw_input()
	
	if auto == "Yes":
		print("Automatic mode!")
		
		dir_list = [
			"auth",
			"channel1/channel1_1",
			"channel1/channel1_2",
			"channel2/channel2_1",
			"channel2/channel2_2",
			"channel3/channel3_1",
			"channel3/channel3_2",
			"channel4/channel4_1",
			"channel4/channel4_2",			
			"game99",
			"mark_server"
		]
		
		core_list = [
			"auth",
			"game1_1",
			"game1_2",
			"game2_1",
			"game2_2",
			"game3_1",
			"game3_2",
			"game4_1",
			"game4_2",
			"game99",
			"markcore"
		]
		
	else:
		while next == 0:
			print("Please input your core name (example: channel1_2): (Type !=! to exit)")
			fx = raw_input()
			if (len(fx) < 1):
				print("Please input something!")
				continue
			
			core_list.append(fx)
			
			print("Now input the directory: (example: channel1/channel1_2)")
			fx = raw_input()
			if (len(fx) < 1):
				print("Please input something!")
				continue
				
			dir_list.append(fx)	

			next = next + 1
	
	print("Installing symlinks...")
	
	print("Doing symlink for share")
	make_share(base, share, locale)
	
	print("Doing symlink for db")
	make_db(base, "db", share)
	
	count = 0
	count_len = len(core_list)

	while count < count_len:
		print("Doing symlink for: " + core_list[count])
		make_core(base, dir_list[count], core_list[count], share)
		count = count + 1
	
	print("Done! (See https://www.rewardmetin2.altervista.org/uriel/doku.php?id=installing_metin2_serverfiles for more information)")
		
entry_point()
