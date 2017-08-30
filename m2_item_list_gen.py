#!C:\Python27\pythonw.exe
## BY ARVES100 (LIVE STREAMING 09)

## OPZIONI ##
vnum = 21110  
type = "ETC"
icon_path = "icon/item/"
gr2_path = "d:/ymir work/item/weapon/"
icon_ext = ".tga"
gr2_ext = ".gr2"
item_list_name = "item_list.txt"

## FINE DELLE PARTI DA MODIFICARE
fp = open(item_list_name,"a")
count = 0

while count < 10:
	cvnum = str(vnum+count)
	fp.write(cvnum + "\t" + type + "\t" + icon_path + str(vnum) + icon_ext)
	
	if type == "WEAPON" or type == "WING":
		fp.write("\t" + gr2_path + str(vnum) + gr2_ext)
	fp.write("\n")
	count += 1
	
fp.close()
print("OK!!!!")