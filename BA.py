# Anuneet Anand
# CSE-112
# Project-2 : Booth's Algorithm

def Int(x):
	''' Finds Decimal Representation Of A Binary Number'''
	s = 1
	if x[0]=="1":
		x = TC(x)
		s = -1
	n = 0
	for i in range(len(x)-1,-1,-1):
		n = n + int(x[i])*(2**(len(x)-i-1))
	n = n * s
	return n

def Ext(B,n):
	''' Extends A Binary Number To Required Number Of Bits''' 
	S = B[0]
	while len(B)<n:
		B = S + B
	return B

def Bin(x):
	''' Converts A Decimal Number To It's Unsigned Binary Representation'''
	B = ""
	while x:
		B = str(x%2) + B
		x = x // 2
	return "0" + B

def TC(x):
	''' Returns Two's Complement Representation Of A UnSigned Binary Number'''
	s = ""
	j = x.rfind("1")
	if (j == -1):
		return "1" + x
	L = list(x)
	for i in range(j):
		L[i] = int(L[i]) ^ 1
	for i in L:
		s += str(i)
	return s

def Num(x):
	if x>=0:
		return Bin(abs(x))
	else:
		return TC(Bin(abs(x)))

def Add(x,y):
	''' Adds Two Binary Numbers '''
	n = max (len(x),len(y))
	r = 0
	c = 0
	z = ""
	for i in range(n-1,-1,-1):
		r = int(x[i])^int(y[i])^c
		c = ( (int(x[i]) ^ int(y[i]) ) & c ) | ( int(x[i]) & int(y[i]) )
		z = str(r) + z
	return z

print("Enter Multiplicand: ",end="")
X = int(input())
print("Enter Multiplier: ",end="")
Y = int(input())

x = Num(X)
y = Num(Y)
l = max(len(x),len(y))
x = Ext(x,l)
y = Ext(y,l)

A = x + "0" * (l+1)
S = Ext(Num(-X),l) + "0" * (l+1)
P = "0" * (l) + y + "0"

for i in range(l):
	if P[-1]=="1" and P[-2]=="0":
		P = Add(P,A)
	elif P[-1]=="0" and P[-2]=="1":
		P = Add(P,S)
	P = P[0]+P[:-1]
P = P[:-1]

print(Int(P))

