import math
import os
os.system('clear||cls')
AFM = input("Что найти?(a,F,m):")
if AFM == "a":
	F=input("F=")
	m=input("m=")
	a= float(F)/float(m)
	input('a='+str(a))
elif AFM == "F":
	m=input("m=")
	a=input("a=")
	F= float(m)*float(a)
	input('F='+str(F))
if AFM == "m":
	F=input("F=")
	a=input("a=")
	m=float(F)/float(a)
	input('m='+str(m))
os.system('clear||cls')