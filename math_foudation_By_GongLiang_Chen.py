
secured communication
data security
computer security
cryptography and technologies(core of information security)
internet security
	truth,integerity,undeniable

infrmation security:
	security:	message not read by unanthencated
	truth:		verify that message was send by the sender
	integerity:	message not changed through info channel
	undeniable:	sender can not deny the sending fact 
				receiver can not deny the receiving fact


non-sysmetrical cipher
	one-way trap function

	0.backpack problem	
	1.large integer decomposition
		RSA, Rabin-William
	2.logrithm problem on Glosis field
		DSA, Diffie-Hellman, ElGamal
	3.logrithm problem on elliptic curve 
		ECC

computational security:
	RSA:	p,q in 1024 bit	sufficient to be safe

#==============================================================

chapter 1 integer divison

#============================================================== 

divison : a=q*b noted as b|a 
	----division is defined by multiplication
    ----if we are to prove b|a ,we need to find q and write a=q*b
    ----0 is multiple to all
    ----1 is factor to all
    ----a is factor and multiple to a

divison characteristics:
	(1)transcendent:
		if  a|b, b|c :
			a|c

	(2)linear combination    
		if  a|b, a|c :
			s,t in integer
			a|s*b+t*c

	(3)equality
		if a|b:
		 if b|a:
		 	a==b

prime
	has only 1 and itself as factor
	minium element of integer multiplication

p: first factor of n must be a prime
	p<sqrt(n)

Eratosthenes methods
	find all primes in range(0~N)
	
	for i in range(0~sqrt(N))
		delete k*i (k=1,2..)

	ramaining numbers are primes

primes are infinite
	construct: p1p2p3...pn+1



pre.theorem 1
	for a,b in integer:
		r == a (mod b)
		2^a -1 == 2^r -1 (mod 2^b -1)

pre.theorem 2
	for a,b in integer:
		(2^a -1 , 2^b -1)=2^(a,b) -1

theorem	(simplify calculation when a,b are 1024 like numbers)
	for a,b in integer:
		if (a,b)==1:
			(2^a -1 , 2^b -1) == 1	

theorem
	for q,r,s,t in integer:
		a=qu+rv
		b=su+tv
		(a,b)=(u,v)


division simplify:
	if c|ab:
		if (a,c)==1		
			c|b

prime divison theorem:
	if p in prime:
		if p|ab:
			p|a or p|b

			
Euclid division
	for a,b in integer:
		exist.unique. q,r
		a=qb+r 
		0<=r<|b|



practical problem:
	how to fast implement Euclid division?
		(to get q,r)
	 b=2^u + v (v is small,u>1024)


simple prime judgement(effective):
	for n < one million:
		for p primes in sqrt(n)
		check if p|n


define [x] function	:max but not over x

Euclid division with general remainder:
	for a,b,c in integer:
		exist.unique. q,r
		a=qb+r 
		c<=r<b+c


base-b number:
	length: k=[log.b.(n)]+1

computational complexity:
	add and sub: O(max(log.2.a, log.2.b))	
	mul and div: O((log.2.a)*(log.2.b))


how to find GCD of two numbers:
	(1)defination method is decomposition and find the superpositioned part
		----large numbr decomposition problem

	(2)succssive divison
		if a=qb+r:
			(way.1 min-non-neg remainder)
			(way.2 min-abs remainder)	
			
			(a,b)==(b,r)

		need n<5 log.b times to find final result 	

	(3)by product:roll back ----Bezout equation
		for a,b in integer:
			exist.s,t
			(a,b)=sa+tb


bezout equation:
	represent(a,b) == sa + tb

	method(1) succesive divison and roll back			

	method(2) recursive producing (proved by matrix arithmetic)
				better for computer programming

		sn*a+tn*b == (a,b)
		
		s[-2] = 1, t[-2]=0
		s[-1] = 0, t[-1]=1

		r[-2] = a, r[-1]=b

	looping:	
		s[j]=(-q[j])s[j-1] + s[j-2]

		t[j]=(-q[j])t[j-1] + t[j-2]

		q[j+1]=[ r[j-1] / r[j-] ]
		
		r[j+1]=(-q[j+1])*r[j] + r[j-1]

	until r[j+1]==0 

		 (a,b) = r[j] 

		 s[j]*a + t[j]*b = (a,b) 	



co-prime judgement:
	for a,b in integer:
		exist. s,t:
			sa+tb = 1

	conclusion:		
		sa+tb = 1  <=> (a,b)=1


co-prime integer construct:
	(1)for a,b,c in integer:
			(am,bm)=(a,b)m

	(2)for a,b,d in integer:
			if d|a, d|b :
				(a/d, b/d) = (a,b) /d 

	result:
		( a/(a,b) , b/(a,b) ) =1



characteristics of GCD:
	(1)simplification of GCD
		for a,b,c in integer:
			if (a,c)==1 :
				(ab,c)=(b,c)




integer unique decomposition
	Standard decomposition
	counting function 
		----number of factors
		----d(n)=Pai(1+ai) 
		----where ai is power in Standard decomposition


construct of common multiple
	for a,b in integer:
		[a,b]=ab/(a,b)


	for a,b,c...z in integer:
		[a,b]=ab/(a,b)
		[a,b,c]=[a,b]c/([a,b],c)
		.
		.
	two-two combination calculation		



modern decomposition of integer:
modern practical RSA attack

	for n in composite number:
		if exist.a,b:
			n|a^2-b^2
			n !| a-b
			n !| a+b
			(a and b are constructed by linked fraction)
	
	(n,a-b) , (n,a+b) are ture factor of n	

#===========================================================
#
chapter 2 congruence

defination:
	for a,b,m in integer:
		exist.q
		a=b + qm

	def a==b (mod m)

characteristics of congruence:
	----(==)(mod ) is a kind of equality operator

	(1) self-congruence
		for a,m in integer:
			a==a(mod m)	

	(2)symmetric:
		for a,b,m in integer:
		if a==b (mod m):
			b==a (mod m)

	(3)transcendent:		 
		if a==b(mod m):
		 if b==c(mod m):
		 	a==c(mod m)


extended characteristics of congruence

	(1) if a==b (mod m):
			m|a-b

	(2)if a==b (mod m):
			a^n ==	b^n  (mod m) # power
			f(a)==	f(b) (mod m) # polynomials


	(3)if a==b (mod m):
		if p==q (mod m):		

			m*a+u*p == n*b+v*q (mod m) 	#linear combination
			ap==bq (mod m)				#production

	(4)if ac==bc (mod m)
		if (m,c)==d:
			a==b (mod m/d)				#canceling

	(5) if a==b (mod mi) for all mi in {mi}:
			a==b (mod [m1,m2,m3..mn])

	(6)root of congruence equation x==a (mod m)
			are {x|x=a+km ,k in Z ring}		








		