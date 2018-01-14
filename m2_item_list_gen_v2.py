#!C:\Python27\pythonw.exe

## Originally coded on Live Stream 09 of Made in Server
## Version 02 coded on 14-01-2018
## If someone is interested about the license, it is MIT (yes it's real)

import sys

def main_func():
	print("Input the vnum: ")
	tt = raw_input()
	if not tt.isdigit():
		print("Please input a number")
		sys.exit(0)

	vnum = int(tt)
	
	print("Input the type:")
	print("(1) WEAPON")
	print("(2) ETC")
	print("(3) ARMOR")
	print("(4) WING")
	tt = raw_input()
	if not tt.isdigit():
		print("Please input a number")
		sys.exit(0)
	
	choice = int(tt)
	have_gr2 = 0
	
	if choice == 1:
		type = "WEAPON"
		have_gr2 = 1
	elif choice == 2:
		type = "ETC"
	elif choice == 3:
		type = "ARMOR"
	elif choice == 4:
		type = "WING"
		have_gr2 = 1
	else:
		print("Unknown choice")
		sys.exit(0)
		
	print("Input icon path: (Press ENTER for default value: \"icon/item/\")")
	icon_path = raw_input()
	if len(icon_path) < 1:
		icon_path = "icon/item/"
	
	print("Input icon extension: (Press ENTER for default value: \".tga\")")
	icon_ext = raw_input()
	if len(icon_ext) < 1:
		icon_ext = ".tga"
		
	if have_gr2 == 1:
		print("Input gr2 path: (Press ENTER for default value: \"d:/ymir work/item/weapon/\")")
		gr2_path = raw_input()
		if len(gr2_path) < 1:
			gr2_path = "d:/ymir work/item/weapon/"
		
		print("Input gr2 extension: (Press ENTER for default value: \".gr2\")")
		gr2_ext = raw_input()
		if len(gr2_ext) < 1:
			gr2_ext = ".gr2"	
	
	print("Input output name: (Press ENTER for default value: \"item_list.txt\")")
	item_list_name = raw_input()

	if len(item_list_name) < 1:
		item_list_name = "item_list.txt"
		
	fp = open(item_list_name,"a")
	count = 0

	while count < 10:
		
		fp.write(str(vnum + count) + "\t" + type + "\t" + icon_path + str(vnum) + icon_ext)
	
		if have_gr2 == 1:
			fp.write("\t" + gr2_path + str(vnum) + gr2_ext)
		fp.write("\n")
		count += 1
	
	fp.close()
	
if __name__ == "__main__":
	print("Item list generator v2.0 by arves100")
	main_func()
	print("Finished!")