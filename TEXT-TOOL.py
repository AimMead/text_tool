import time
import os
def atx(attari):
    os.system(attari)
atx('color a')
print("\t\t\t\t  <--Text Tool-->")
print("\t\t\t\t<-By Mostafa Mead->")
print("\t\t\t\t<-Github/AimMead->")
print("\t\t\t\t<-FB/100010261237574->")
print("")
print("\t[1] Remove Duplicates")
time.sleep(.2)
atx('color e')
print("\t[2] Get Email:Pass Combo From Text")
time.sleep(.2)
atx('color a')
print("\t[3] Get Emails From Combo")
time.sleep(.2)
atx('color e')
print("\t[4] Email:Pass To User:Pass")
time.sleep(.2)
atx('color a')
print("\t[5] Add Domain To User:Pass Combo")
time.sleep(.2)
atx('color e')
print("\t[6] Add Prefix/Sufix Into Line")
time.sleep(.2)
atx('color a')
print("\t[7] Filter Email")
print("")
what = input("\tWhat Do You Want : ")

def removeDuplicates(path):
	dup = []
	print("\tremoveingDuplicates..")
	with open(path) as f:
		lines = f.read().split("\n")
	for line in lines:
		dup.append(line)
	a = set(dup)
	for i in a:
		text_good = open("Duplicated.txt" , 'a+')
		text_good.write(i + "\n")
		text_good.close()
def getFromText(path):
	with open(path) as f:
		lines = f.read().split("\n")
	for line in lines:
		if ":" in line:
			text_good = open("getFromText.txt" , 'a+')
			text_good.write(line + "\n")
			text_good.close()
def getFromCombo(path):
	with open(path) as f:
		lines = f.read().split("\n")
	for line in lines:
		if "@" in line:
			text_good = open("EmailFromCombo.txt" , 'a+')
			text_good.write(line + "\n")
			text_good.close()
def emailPassToUserPass(path):
	with open(path) as f:
		lines = f.read().split("\n")
	for line in lines:
		user = line.split(":")[0].split("@")[0]
		password = line.split(":")[1]
		text_good = open("emailPassToUserPass.txt" , 'a+')
		text_good.write(str(user) +":"+str(password) + "\n")
		text_good.close()
def addDomain(path , domain):
	with open(path) as f:
		lines = f.read().split("\n")
	for line in lines:
		user = line.split(":")[0]
		password = line.split(":")[1]
		email = user + "@" + str(domain)
		text_good = open("addDomain.txt" , 'a+')
		text_good.write(str(email) +":"+str(password) + "\n")
		text_good.close()
def Prefix(path , prefix):
	with open(path) as f:
		lines = f.read().split("\n")
	for line in lines:
		d = str(prefix) + line
		text_good = open("Prefix.txt" , 'a+')
		text_good.write(str(d) + "\n")
		text_good.close()
def Sufix(path , sufix):
	with open(path) as f :
		lines = f.read().split("\n")
	for lin in lines:
		d = lin + str(sufix)
		text_good = open("sufix.txt" , 'a+')
		text_good.write(str(d) + "\n")
		text_good.close()
def filterEmail(path):
	with open(path) as f:
		lines = f.read().split("\n")
	for line in lines:
		if "aol" in line:
			aol = open("aol.txt" , 'a+')
			aol.write(line + "\n")
		elif "comcast" in line:
			comcast = open("comcast.txt" , 'a+')
			comcast.write(line + "\n")
		elif "gmail" in line:
			gmail = open("gmail.txt" , 'a+')
			gmail.write(line + "\n")
		elif "gmx" in line:
			gmx = open("gmail.txt" , 'a+')
			gmx.write(line + "\n")
		elif "hotmail" in line:
			hotmail = open("hotmail.txt" , 'a+')
			hotmail.write(line + "\n")
		elif "outlook" in line:
			outlook = open("outlook.txt" , 'a+')
			outlook.write(line + "\n")
		elif "yahoo" in line:
			yahoo = open("yahoo.txt" , 'a+')
			yahoo.write(line + "\n")
		else:
			other = open("other.txt" , 'a+')
			other.write(line + "\n")
if what == "1":
	removeDuplicates(input("\t\tEnter Path : "))
	time.sleep(10000)
elif what == "2":
	getFromText(input("\t\tEnter Path : "))
	time.sleep(10000)
elif what == "3":
	getFromCombo(input("\t\tEnter Path : "))
	time.sleep(10000)
elif what == "4":
	emailPassToUserPass(input("\t\tEnter Path : "))
	time.sleep(10000)
elif what == "5":
	addDomain(input("\t\tEnter Path : ") , input("\t\tEnter Domain [Ex:yahoo.com] : "))
	time.sleep(10000)
elif what == "6":
	print("\t\t[1] Add Prefix")
	print("\t\t[2] Add Sufix")
	boss = input("\t\t\tGive A Number : ")
	if boss == "1":
		Prefix(input("\t\tEnter Path : ") , input("\tEnter Text : "))
		time.sleep(10000)
	elif boss == "2":
		Sufix(input("\t\tEnter Path : ") , input("\tEnter Text : "))
		time.sleep(10000)
elif what == "7":
	filterEmail(input("\t\tEnter Path : "))
	time.sleep(10000)
else:
	print("Please Choose A Right Number")
print("\t\tDONE >--<")
time.sleep(100)