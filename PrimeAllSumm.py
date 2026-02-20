from sympy import *

primes = [x for x in range(3,100001) if isprime(x)]

prime=0
notprime=0

x = {}
xT={}


#для любого простого числа n > 3 есть простое число n2<n, так, что n+n2=s, где s лежит на расстоянии 1 от простого числа
#подтвержденно до 100к
for i in range(1,len(primes)-1):
		x[primes[i]] = []
		for i2 in range(i):
			x[primes[i]].append(primes[i]+primes[i2])
		
for k in x:
		flag = 0
		xT[k]=0
		for n in x[k]:
			xT[k]+=1
			if isprime(n+1) or isprime(n-1):
				prime+=1
				flag = 1
				break
		if flag == 0:
				notprime+=1
		else:
				flag=0			
		
		
print(prime,notprime)
#print(xT)

#для любого простого числа n>5 существует два меньших простых числа n0,n1, так, что n0+n1=s, где s лежит на расстоянии 1 от n


results = {}
c,c2 = 0,0

for i in range(2, len(primes)):
    p = primes[i]
    found = False
    for j in range(i):
        q1 = primes[j]
        for k in range(j, i):
            q2 = primes[k]
            s = q1 + q2
            if s == p - 1 or s == p + 1:
                results[p] = (q1, q2, s - p) 
                found = True
                break
        if found:
            c+=1
            break
    if not found:
        c2+=1
        

print(c,c2)
