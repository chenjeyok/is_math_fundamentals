
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
#

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

			