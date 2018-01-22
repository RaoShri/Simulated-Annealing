import random
import math


A = [[0,1,2,3,2,4],[1,0,1,4,2,1],[2,1,0,3,2,1],[3,4,3,0,4,3],[2,2,2,4,0,2], [4,1,1,3,2,0]] 		# Adjacency matrix A[i][j]
#A = [[0,1,0,0,0,0],[1,0,0,1,0,0],[0,0,0,1,0,1],[0,1,1,0,1,0],[0,0,0,1,0,1], [0,0,1,0,1,0]]


n = len(A)

T=50
r= 0.9
cut_cost = 0
cut_ratio=0
cost = 0 
balance = 0

current_cut_cost = 0
current_cut_ratio = 0
current_cost = 0
current_balance =  0 

lamb = 0.05	
delta = 0

X = []
Y = []
X_new=[]
Y_new=[]
l1 = n/2
l2 = n/2


i=0;
while i < l1:
   X.append(i)
   i=i+1
while i < n :
   Y.append(i)
   i=i+1
print "\nInitial Partition : "
print "X : ", X, "Y : ", Y

#Initial computation

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

print "Cut Cost : ", current_cut_cost
print "Cut Ratio : ", current_cut_ratio
print "Balance Factor: ", current_balance
print "Total Cost : ", current_cost,'\n'

accept = 0
l1_old =n/2
l2_old =n/2
p=100
while T > 0.3:
	for trials in range(p):
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
		
		
		
		if accept > 10:
			break	
	T = r*T


print "Final Partition : "
print "X : ", X, "Y : ",Y
print "Cut Cost : ", current_cut_cost
print "Cut Ratio : ", current_cut_ratio
print "Balance Factor: ", current_balance
print "Total Cost : ", current_cost,'\n\n'
