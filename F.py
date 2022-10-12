import math
import os
os.system('clear||cls')
AFM = input("Что найти?(a,F,m):")
if AFM == "a":
	F=input("F=")
	m=input("m=")
	a= float(F)/float(m)
	print(a)
elif AFM == "F":
	m=input("m=")
	a=input("a=")
	F= float(m)*float(a)
	print(F)
if AFM == "m":
	F=input("F=")
	a=input("a=")
	m=float(F)/float(a)
	print(m)
input()
os.system('clear||cls')