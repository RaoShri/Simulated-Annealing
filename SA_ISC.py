# Implementation of Simulated Annealing for partition of graphs
# Author Shrinidhi Rao
# Date : 21/08/2018


import random
import math
import numpy as np
import sys

A= sys.argv[1]


# Get Adjacency Matrix
def Get_matrix(x):
 
   y=len(x)
   list=x
   Matrix=np.zeros((y,y))
   for i in list:
	for j in list:
	   for o in range(1,10):
		if j[o]==i[0]:
		     j[o]=i[10]
 
   for i in list:
	for o in range(1,10):
		if i[o]!='0' and i[o]!=0:
			Matrix[int(i[10])-1][int(i[o])-1]=1
			Matrix[int(i[o])-1][int(i[10])-1]=1
 
   return Matrix


# Removing extra characters
def node(line):
   xy=[]
   z=0
   a="\0"
   if line[0]!="*":
	for i in line:
		if i=="*":
			p=[a.strip("\x00") for a in xy]
			return p
		elif i!=" " and i!="\n":
			a+=i
			z=1
     		else:
			if z==1:
				xy.append(a)
				a="\0"
				z=0
   p=[a.strip("\x00") for a in xy]
   return p


# Obtaining Adjacency list from Netlist (.isc file)

def Get_Adjacency_List(filename):
   f=open(filename,"r");
   line=f.readline()
   c=0;
   a=[]
   y=['','','aaa']
   record=[]
   count=1
   while line:
	y_new=node(line)
	if y_new:
		if y[2]!="from" and y[2]!="inpt" and y[2]!="aaa":
    
			x=[y[0],y_new[0],y_new[1] if int(y[4])-1>0 else 0,y_new[2] if int(y[4])-2>0 else 0,y_new[3] if int(y[4])-3>0 else 0,y_new[4] if int(y[4])-4>0 else 0,y_new[5] if int(y[4])-5>0 else 0,y_new[6] if int(y[4])-6>0 else 0,y_new[7] if int(y[4])-7>0 else 0,y_new[8] if int(y[4])-8>0 else 0,count];
			count+=1
			a.append(x)
			y=['','','aaa']
		else:
			y=y_new
			record.append(y_new)
	line=f.readline()
   f.close()
   z=a;
 
   tag=1
   while tag==1:
	tag=0
	for s in z:
		for row in record:
			for u in range(1,10):
				if s[u]==row[0]:
					if row[2]=="from":
						tag=1
						for i in record:
							if row[3]==i[1]:
								s[u]=i[0]
   z1=z

 
   for s in z1:
	t=9*[0]
	for d in a:
		for u in range(1,10):
			if s[u]==d[0]:
				t[u-1]=1
	for u in range(0,9):
		if t[u]==0:
			s[u+1]=0
 
   return z1

A = Get_Adjacency_List(A)
A = Get_matrix(A)

n = len(A)

#These Values should be tuned according to the problem
T=5
r= 0.9
lamb = 0.05

#Cost Parameters
cut_cost = 0
cut_ratio=0
cost = 0 
balance = 0

current_cut_cost = 0
current_cut_ratio = 0
current_cost = 0
current_balance =  0 

	
delta = 0

X = []
Y = []
X_new=[]
Y_new=[]
l1 = n/2
l2 = n/2

#Initial Partition
i=0;
while i < l1:
   X.append(i)
   i=i+1
while i < n :
   Y.append(i)
   i=i+1
print "\nInitial Partition : "
print "X : ", X, "Y : ", Y

#Initial computation of cost

i=0
while i < l1:
   j=0
   while j<l2:
	current_cut_cost += A[X[i]][Y[j]]
	j+=1
   i+=1
current_cut_ratio = current_cut_cost/float((l1*l2))

current_balance = (l1-l2)**2

current_cost = current_cut_ratio + lamb * current_balance

print "Number of elements in Partition X : ", l1
print "Number of elements in Partition Y : ", l2
print "Cut Cost : ", current_cut_cost
print "Cut Ratio : ", current_cut_ratio
print "Balance Factor: ", current_balance
print "Total Cost : ", current_cost,'\n'

accept = 0
l1_old =n/2
l2_old =n/2
p=1000
counter = 0;

#Annealing process
while T > 0.01:
	for trials in range(p):
		counter+=1		
		l1 = random.randint(1,(n-1)) 
		l2 = n - l1
		cut_cost = 0
		X_new = random.sample(range(0, n), l1)
		j=0
		while j < n:
		   if j not in X_new :
			Y_new.append(j)
		   j+=1

		#Cost of the second solution

		i=0
		while i < l1:
		   j=0
		   while j < l2:
			cut_cost += A[X_new[i]][Y_new[j]]
			j+=1
		   i+=1
		cut_ratio =cut_cost/float((l1*l2))

		balance = (l1-l2)**2

		cost = cut_ratio + lamb * balance
		delta = cost - current_cost
		if ((delta < 0) or (random.uniform(0,1) < math.exp( -(delta/T) ) ) ) :
		     
		   for node in range(l1_old):
			X.pop(0)

		   for node in X_new :
			X.append(node)
		   	
		   
	

		   for node in range(l2_old):
			Y.pop(0)

		   for node in Y_new :
			Y.append(node)
	
		   
		   current_cut_cost = cut_cost
		   current_cut_ratio = cut_ratio
		   current_balance = balance
		   current_cost = cost
		   l1_old = l1
		   l2_old = l2
		   accept +=1		
		for node in range(l1):
			X_new.pop(0)	

	
		for node in range(l2):
			Y_new.pop(0)
		
		
		
		if (accept > 10*n) or (counter > 100*n):
			break	
	T = r*T


print "Final Partition : "
print "X : ", X, "Y : ",Y

print "Number of elements in Partition X : ", l1_old
print "Number of elements in Partition Y : ", l2_old
print "Cut Cost : ", current_cut_cost
print "Cut Ratio : ", current_cut_ratio
print "Balance Factor: ", current_balance
print "Total Cost : ", current_cost,'\n\n'
