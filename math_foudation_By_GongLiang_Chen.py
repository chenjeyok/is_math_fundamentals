
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

chapter 2 congruence

#==========================================================

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
			ak==bk(mod mk):		

	(4)canceling 1

	if ac==bc (mod m):
		if (m,c)==1:
			a==b (mod m)				

	  canceling 2
	  	
		if a==b(mod m:
			if d != 0:
				if d|(a,b,m):			
					a/d==b/d(mod m/d)  

		----because no zero factor in the field


	(5) if a==b (mod mi) for all mi in {mi}:
			a==b (mod [m1,m2,m3..mn])

		eg.RSA encription
		m^e==c mod n
		
		m^e==c==c1 mod p
		m^e==c==c2 mod q

		send c1,c2

		receiver decript :
			x==c1 mod p
			x==c2 mod q

		eg.
			for p,q in prime:
				if a==b (mod p)
				if a==b (mod q)
					a==b (mod pq)	

	(6)root of congruence equation x==a (mod m)
			is a residue class {x|x=a+km ,k in Z ring}		


	(7)a,b in same class and has similar characteristic
		if a==b(mod m):
			(a,m)==(b,m)

	(8)congruence equations simplification:
	if a==b (mod m)
		for d in factors of m:
		 	d|m
		 	a==b(mod d)

	eg.
		x==b1 mod 6
		x==b2 mod 10
		x==b3 mod 15

		simplify to mod prime:
			x==b1 mod 2
			x==b1 mod 3

			x==b2 mod 2
			x==b2 mod 5
			
			x==b3 mod 3
			x==b3 mod 5


congruence is to classify integers:
	
	Ca={c|c==a(mod m),k in integer}

	----Ca is 'a' number on operation ==(mod m)
	




Euler function fai()
	(1)
	for p,q in prime:
		n=pq
		fai(n)=fai(p)fai(q)
	
	(2)factor fai(d) sum makes self
	for d in factor of n:
		Sigma(fai(d))=n

	(3)Euler theorem
		if (a,m) ==1 
			a^fai(m)==1 (mod m)

	(4)fermat (an special value of Euler theorem)
		for p in prime:
			a^p   == a(mod p)
			a^p-1 == 1(mod p)
	(5)Willson
		(p-1)!  == -1(mod p)					



decomposition of congruence equation of modulus prime p

	x^3 + 2013x^2 - 2011x -3 = 0



calculate:
	b^16	b^17	b^128
	periodic sequence	->	RSA  is fairly resonable
	period fai(n) is in core effect

mod power repeation method:
	large module m
	large integer n

	b^n mod m

	first represent n as binary form {n0,n1,n2,n3...nk}

	b^n = b^n0 * (b^2)^n1 * (b^4)^n2 .. * (b^(2^k)) ^ nk

	there are 3 sets of sequence {ai} {bi} to trace from:
		(1){bi} are the binary powered b table
			b0=b
			b1=b0^2=b^2
			b2=b1^2=b^4
			.
			bk=(b[k-1])^2 = b^(2^k)

		(2){ni} is the binary representation of n
			----to control if bi is to multiply into the result

		(3){ai} is actually accumulated	result controled by {ai}

		steps:
		
		make table ni:	represente n in binary form


		make table bi:	bi=b[i-1]^2 (mod m)
			---- can be done along with ai
			---- the essence is that its independent to ai
		
		if ni==1:
			accumulate ai:	ai = a[i-1] * bi 	(mod m)
		else:
			remaining ai:	ai = a[i-1]




RSA:
	key generator:

		choose p,q:
		calculate: n=pq ,fai(n)=(p-1)(q-1)
			----Plaintext space N^k having k chars
			----cipher space N^l having l chars
			----(N^k < N^l) to have full map N^k -> N^l 
			----(N^k <n< N^l) to have security issues(to be explained)

		choose e randomly where (e,fai(n))==1 and  0<e<fai(n)
			----encription key gen
			----e shall be not to large for efficiency

		solve equation: de == 1(mod fai(n)) 	
			----solve congruence equation find Bezout expression of (e,fai(n))
			----guaranted by (e,fai(n)) == 1
			----decription key gen
			----thus to have de=1+k*fai(n) which is the nuence of RSA

	encription:
		
		message digitalize M: encode 
			----haffman,simple
		cipher C:	C=M^e (mod n)
			----mod repeating squared method

	decription:

		Clear text:	M=C^d (mod n)
			----mod repeating squared method
			----C^d == M^de == M^(1+k*fai(n)) mod n
				----congruence characteristic 1: multiply
				----Euler theorem 
						for p,q in prime:
							M^fai(p) == 1 (mod p)
							M^fai(q) == 1 (mod q)
							thus:
							M^fai(n) == 1 (mod n)
				----thus M^(1+k*fai(n)) == M (mod m)
	


#==============================================================

chapter 3 congruence equation

#============================================================== 

def congruence equation:
	f(x) == 0 (mod m) 
	where f(x) is a polynomial

def solution to congruence equation:
	
	Ca={x|for x in integer: x==a(mod m)}
		----ressidue classes that meet the equation
		----residue class is the min multiply unit in (==(mod m)) equality classification

1st powered congruence equation
	
	ax==b (mod m)

	(1)method 1:
	solution:
		----valid if (a,m)|b

	for a,m in integer:
		Succesive divison getting (a,m)
		roll back (a,m) = sa + tm
			----or use Bezout generator algorithm
		if (a,m)|b:
			multiple the expression: sq*a+tq*m = b 
			solution: x1 == sq(mod m)
			----particular solution

	(2)method 2:

	general solution:
	x==x1 +  t*m/(a,m) (mod m)		
	
	general form:	
	x==b/(a,m)( (a/(a,m))^-1 (mod  m/(a,m) )) +  t*m/(a,m) (mod m)		

	basic idea is:
		solve (a/(a,m)) x ==1 (mod  m/(a,m) ):
			----a/(a,m) and m/(a,m) are co-primed
			----a/(a,m) in RRC thus there is a inverse of it
			----x0==a/(a,m)^-1 (mod  m/(a,m) )

		observe: (a/(a,m)) x ==b/(a,m) (mod  m/(a,m) )
			----solution is constructed x0*b/(a,m)

		its also a solution to: ax==b (mod m)		 		

def inverse on Galosis Field by mod m:
	if a''a == 1 (mod m):
		a'' is inverse of a on this GF


reduced residue system (RRS) self-inverse:

	(1)
	for a in reduced residue systems by mod m:
		a'' == a

	(2)
	if a''== a:
		a in one reduced residue class (RRC) by mod m


china residue theorem
	congruence equations set
	
	{mi}
	{mi} co-primed

	m=Pai(mi)

	for mi in {mi}:  
		Mi == n/mi
		M'i'*Mi == 1 (mod m) 
			----inverse


	solution: x=Sigma(bi * M'i'Mi) mod m
		----where bi is considered variable
		----M'i',Mi are considered relativly static
 

congruence equations and cloud computing:
	final result and a small part done by self 
	most part gives to cloud

Rabin cipher:
	encription:
		for p,q in prime:
			n=pq
			m^2==c (mod n)
		
	decription:
		solve x^2==c mod n equivalent:
		solve quadrtic congruence equation
		x^2==c mod p
		x^2==c mod q
			---- solution x==b1 mod p
			---- solution x==b2 mod q		

		use china residue theorem:	
			x==p^-1 (mod q) qb1 + q^-1(mod p) pb2 	(mod pq)



china residue theorem to decomposite problem
	x==b(mod m)

	use congruence equations to represent this problem:
	x==b(mod m1)
	x==b(mod m2)
	x==b(mod m3)
	x==b(mod m4)


#=======================================================================

chapter 4 quadratic congruence equation

#=======================================================================

def quadratic residue:
	
	x^2==a(mod m)  where (a,m)=1

in reduce residue system of mod p:
	quadratic residue and quadratic non-residue each has 1/2 
	equal calssify



quadratic residue judgement:
	(1)Euler judgement:
		for p in odd prime:
			if (a,p)==1:
				X^2 == a (mod p)

				a^[(p-1)/2]== 1	has solution
				a^[(p-1)/2]==-1	no  solution

		Legendre form:
			(a/p) == a^[(p-1)/2]


	(2)results(++=+, --=+, +-=-):
		if a1,a2 are QuadResd to x^2==a (mod p):
			a1*a2 is QuadResd

		if a1,a2 are Quad-non-Resd to x^2==a(mod p):
			a1*a2 is QuadResd

		if a1 is QuadResd while a2 is Quad-non-Resd:
			a1*a2 is Quad-non-Resd

	(3)essential concepts of Legendre: foundations to implemente transformation
		
		p in odd prime

		(1/p) ==   1
		(-1/p)==(-1)^[(p-1)/2]

			if p==4k+1:
				(-1/p)== 1

			if p==4k+3:
				(-1/p)==-1

	(4)characteristics of Legendre notation:
		
		p in odd prime 

		(a+p /p) == (a/p)
			----periodic			

		(ab /p)  == (a/p) (a/p)
			----multiply explaining (2) 

		(a^2 /p) == 1 when (a,p)==1
			----squared

		(a/p) == (b/p) when a==b(mod p)
			----conLegendre when congruence

	(5)Gauss pre-theorem
		p in odd prime
		
		(2/p) == (-1)^[(p^2 - 1)/8]		

		(a/p)=-1 ^ T(a,p) 
			when (a,2p)==1
			where T(a,p)== [k== 1~(p-1)/2] Sigma (  [ak/p]  )

	(6)quadratic reciprocal law
		(q/p)(p/q)==(-1)^((p-1 /2)(q-1 /2))


	(*)def Legendre (a/p)
			(a/p)=1  if a is QuadResd
			(a/p)=-1 if a is Quad-non-Resd
			(a/p)=0  if p|a

	(*)for p in odd prime:
		for Cr in mod p reduced residue class:
			QuadResd and Quad-non-Resd are equal numbered


Jacobi judgement of QuadResd
	----as an extension to Legendre notation
	
	(1) (a+m /m) == (a/m)
			----periodic

		(ab/m) == (a/m)(b/m)
			----multiply

		(a^2/m) == 1 when (a,m)==1
			----squared

	(2)basic concepts Jacobi :extended form of Legendre			

		(1/m) == 1

		(-1/m)== (-1)^(m-1 /2)

		(2/m) == (-1)^((m^2 -1)/8)


	(3) Jacobi quadratic reciprocal law

		for n,m in odd numbers 
			n,m can decomposite as product of odd prime {pi}
			
			(n/m) = (-1)^(m-1 /2)(n-1 /2) (m/n)	
	

	(*)def Jacobi notation:

		for pi in odd prime:
			m=Pai(pi)

		(a/m)==(a/p1)(a/p2)...(a/pk)	


		(a/m)== 1 <== has solution 
			----the reversed side not valid
		(a/m)==-1 ==> no solution



quadratic congruence equation solutions
	
	(1) mod p squared root

		for p as 4k+m prime:
			if x^2== a(mod p) has solutioin
			solution will be as
			x== +_ a^(p+1 /4) (mod p)

	
	(2)	for p,q as different 4k+m prime:
			if (a/p) == (b/q) == 1 (has solution)
			as
			x== +_ a^(p+1 /4) (mod p) *s*q +_ a^(q+1 /4) (mod p) *t*p

			(Rabin combinating china residue theorem)


	(3)mod m squared root:
		
		for m in composite number:
			considering:
				x^2 == a (mod m), (a,m)=1
			
				m=2^d * p1^a1 * p2^a2 ... pk^ak
				
			(3.1) for p in odd prime:
					m==p^k

					x^2==a(mod p^k)

					solution judgement:
						(a/p)== 1 has 2
						(a/p)== 0 has 1
						(a/p)==-1 has None
					solution counts:
	
						T=1+(a/p)
						2,1,0 for situations above


			(3.2) if p==2 :
					m== 2^k

					x^2==a(mod 2^k)

					solution judgement:
						if k==2: a==1(mod 4)
						if k>=3: a==1(mod 8)

					solution counts:
						if k==2: has 2
						if k>=3: has 4	


 	(4) x^2+y^2=p judgement:
 		for p in primes:
 			x^2+y^2=p has solution when
 			p==2 or p==4k+1


			
#===========================================================

chapter 5 

#===========================================================

s(a)={ak=a^k mod m|k in natural numbers}

problems:
	(1) is {s(a)} periodic ?
	(2) how to get is period?
	(3) how to get min T of {s(a)} ---- p(a)?
	(4) how to get common period p(a,b) of {s(a),s(b)}?
		and get p(a,b)=[p(a),p(b)]?
	(5)for mi in each-other co-primed
		is there {s(c)} whose p(c)=[p(m1),p(m2)...p(mk)]?
	(6)		







