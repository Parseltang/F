import math
import os
os.system('clear||cls')
print("Сила:\nF;a;m1")
print("Плотность:\nV;Ro;m2")
Formula = input("Что найти?:")
#F a m
if Formula == "a":
	a=input("F=")
	b=input("m=")
	c= float(a)/float(b)
	input('a='+str(c))
elif Formula == "F":
	a=input("m=")
	b=input("a=")
	c= float(a)*float(b)
	input('F='+str(c))
elif Formula == "m1":
	a=input("F=")
	b=input("a=")
	c=float(a)/float(b)
	input('m='+str(c))
#V Ro m
elif Formula== "V":
	a=input("m=")
	b=input("Ro=")
	c=float(a)/float(b)
	input('V='+str(c))
elif Formula == "Ro":
	a=input("m=")
	b=input("V=")
	c=float(a)*float(b)
	input('m='+str(c))
elif Formula == "m1":
	a=input("Ro=")
	b=input("V=")
	c=float(a)*float(b)
	input('m='+str(c))









os.system('clear||cls')