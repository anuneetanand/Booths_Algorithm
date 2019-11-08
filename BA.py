# CSE-112
# Project-2 : Booth's Algorithm
# Anuneet Anand (2018022)
# Pruthwiraj Nanda (2018075)
import time
start_time = time.time()

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
	''' Returns Two's Complement Representation Of An Unsigned Binary Number'''
	s = ""
	j = x.rfind("1")
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
	x=Ext(x,n)
	y=Ext(y,n)
	r = 0
	c = 0
	z = ""
	for i in range(n-1,-1,-1):
		r = int(x[i])^int(y[i])^c
		c = ( (int(x[i]) ^ int(y[i]) ) & c ) | ( int(x[i]) & int(y[i]) )
		z = str(r) + z
	return z

def Multiply(X,Y):
	''' Multiplication Algorithm '''
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
	return Int(P)

def Divide(X,Y):
	''' Division Algorithm '''
	if (Y==0):
		print("Invalid Input! Divisor Can't Be Zero!")
		return
	x = Num(X)
	y = Num(Y)
	l = max(len(x),len(y))
	x = Ext(x,l)
	y = Ext(y,l)
	qs = int(x[0])^int(y[0])
	rs = int(x[0])

	Q =  Ext(Num(abs(X)),l)
	R = "0" * (l+1)
	A =  Ext(Num(abs(Y)),l)
	B =  Ext(Num(-abs(Y)),l)

	for i in range(l):
		if R[0]=="1":
			R = R[1:] + Q[0]
			R = Add(R,A)
		else:
			R = R[1:] + Q[0]
			R = Add(R,B)
		if R[0]=="1":
			Q = Q[1:] + "0"
		else:
			Q = Q[1:] + "1"
	if R[0]=="1":
		R = Add(R,A)

	if qs == 1:
		Q = TC(Q)
	if rs == 1:
		R = TC(R)

	return Int(Q),Int(R)

print("Select An Operation:- ")
print("1: Multiplication")
print("2: Division")
c = input()

for i in range(1,1000):
	for j in range(1,1000):
		if (i*j)!=Multiply(i,j):
			print(i,j)
		Q,R = Divide(i,j)
		if (i//j)!=Q or (i%j)!=R:
			print(i,j)
print("--- %s seconds ---" % (time.time() - start_time))

if c == "1":
	print("Enter Multiplicand: ",end="")
	X = int(input())
	print("Enter Multiplier: ",end="")
	Y = int(input())
	P = Multiply(X,Y)
	print("Product: ",P)

elif c == "2":
	print("Enter Dividend: ",end="")
	X = int(input())
	print("Enter Divisor: ",end="")
	Y = int(input())
	Q,R = Divide(X,Y)
	print("Quotient: ",Q)
	print("Remainder: ",R)

else:
	print("Invalid Choice!")

