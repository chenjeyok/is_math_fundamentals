class introduction:

	3 math hard problems:
		(1)large integer discompose:no practical algorithms
			----computational security
			----RSA foundation
		(2)discret logrithm problems:
		(3)ECC elliptic curve discret logrithm problems:
			----forward computation is straight,backward computation is hard

	syllbus:
		(1)algebra
		(2)number theorem
		(3)logic


#=================================================================

chapter 1 algebra and encode

section 1.1 basic concepts of group		

concepts:	
	modern algebra are based on set
		----things with a common attribute are in a set
	Two operand operation on set
		---- S * S ->S ,(x,y) -> z

group defination:
	for a tuple of 3 (G,*,1): 
		 G is set
		 * is a 2 operand operation
		 1 is an element of G
	
	there are:
		G1(operator associative): for a,b,c in set G:
									a*(b*c) = (a*b)*c 

		G2(unit law)			: for a in set G:
									exist. 1	
									1*a == a*1 == a

		G3(operational inverse)	: for a in set G:
									exist. a' in G			                                         
									a*a' == a'*a ==1

	for G having G1,G2,G3:
		def G group

varients:

	for G having G1,G2	:
		def G half group(with unit without inverse)


	G4(commutaive law)		: for a,b in set G:
								a*b == b*a 

	for G having G1,G2,G3,G4:
		def G commutaive group

	for G having G1,G2,G4:
		def G commutaive half group(with unit without inverse)


summary of group definations:
	G1,G2 makes half group
	adding G3 makes (default) group
	adding G4 makes commutaive half group 				
	adding G3,G4 makes commutaive group
			

section 1.2 instances of group:
	(1) for tuple(Z,+,0):
			Z is int set
			+ is plus operator
			0 is int 0

		there are G1,G2,G3,G4 thus to have commutaive group

	(2) for tuple(Q*,*,1):
			Q* is rational number except 0
			* is multiplication
			1 is rational int 1

		there are 
			G1
				for a,b,c in Q*:
					(a*b)*c == a*(b*c)
			G2
				for a in Q*	:
					exist.1
					a*1 == 1*a ==a
			G3
				for a in Q*	:
					exist a''
					a*a'' == 1
			G4
				for a,b in Q*:
					a*b == b*a

		thus Q* makes commutaive group
		
	(3)eg. hill cipher:

		encription:
			for key M in matrix Lm(Z[26]):
				(y1,y2,y3...ym) = (x1,x2,x3...xm)*M mod 26

		decription:
			for key M in matrix Lm(Z[26]):
				exist M^-1 
				(x1,x2,x3...xm) == (y1,y2,y3...ym)* M^-1 mod 26

		

		in this eg. key M on Lm(Z[26]) which makes a group



#=======================================

section 1.3 subgroup

defination of sub group:
	
	for tuple(G,*,unit):
		G contains A
		unit in A
		(A,*,unit) makes (default) group

	def A subgroup of G(noted as A<=G)


	eg. nZ={...-3n, -2n, -1n, 0, 1n, 2n, 3n...}

		for tuple(Z,+,0):
			Z contains nZ
			0 in nZ
			(nZ,+,0) has:
				G1 
					for Pn,Qn,Rn in nZ:
						Pn+(Qn+Rn) == (Pn+Qn)+Rn
				G2
					for Pn in nZ:
						exist. operational unit 0
						Pn+0 == 0+Pn == Pn
				G3
					for Pn in nZ:
						exist. -Pn		
						-Pn + Pn == unit 0


				making a (default) group
	
#==========================================================
#
section 1.4 repeatative group

defination of repeatative group:
	for I in set G:
		I is power of a

	def G rep group by a(noted as G=<a>)
		a is geneartor of G	


concepts of rank of element I:
	defination:
		for a Generator in group G:		
			a^n == unit 1
		def rank of a == n

	catagories of G:
		for I in set G:
			I ==a^n		
			n == inifite: 
		
			def G inifite rep group

		for I in set G:
			I ==a^n
			n == finite
		
			def G rep group of rank n:
				where G=<a>={1, a, a^2 ... a^n-1} set hase total n elements





#=========================================================

section 1.5 symmetrical group

defination of substitution
	
	for inverse map sig(S->S) on S:
		S={1, 2, 3, 4, ... n}
	def map S->S substitution on S


symmetrical group

	for map Sig in Sn:
		Sig is any one substitution
		Sn is set of all possible substitution
		1 is identical substitution
		Sig(i) is image of element in S under substitution Sig

		for Sig,Yita in Sn:
			[Sig*Yita](i) == Sig(Yita(i))  (functional compound law)

		def symmetrical group of power n (Sn,*,1)
			
			power n comes from S={1, 2...n}
			group element is map ,is substitution
			group operator is map compound
			group unit is identical substitution


instance of symmetrical group:
	(1)permutation cipher
		
		encription:

		for key Sig() in Sm:
			(Sm,*,1) makes a symmetrical group of power m
			unit 1 is identical substitution
			* operation is map compound

			(y1,y2...ym)=(Sig(x1), Sig(x2)...Sig(xm)) 


		Theres no encode ,just position swapping:

		slice plaintext into m-letter chunks
		 for chunk in chunks:
		 	swap position of letters by Sig()


		 decription:
		 	inverse substitution Sig^-1()	
	
	(2)substitution cipher

		encription:
			for key sig() in S26:
			(S26,*,1) makes a symmetrical group of power 26
			unit 1 is identical substitution
			* operation is map compound

			(d, e, ...y)=(Sig(a), Sig(b)...Sig(z)) 

		Its letter substitution like a linkage table

		for letter in letters:
			substitute letter by Sig()

		----vulnerable to frequency attack
		
#======================================================


section 1.6 discret logrithm on group
	
Useful groups on Zn and Z*n:

	for n in integer:
		Zn =={0, 1, ...n-1}
		*mod n is modules multiplication
		tuple(Zn,*mod n,1) has G1,G2 and G4 making commutaive half group
			----tuple as all map on Zn, element are Sig(),Yita()...etc
		1 is operational unit of this commu half group
		
		tuple(Zn,*mod n,1) dont make a group
		
		for n in prime int:
			for a in Z*n={1, 2 ... n-1}:
				exist. a''in Z*n: 
					a'' * a ==1 mod n

		which means (Z[n],*mod n,1) makes commutative group


defination of power of a on Zn:
	
	def a^m == a (*mod n) a (*mod n) a (*mod n) a (*mod n).... 

defination of logrithm problem on group:
	for n in prime int:
		for a,b in Z*n:
	
	def log prob on group:
		find x where a^x = b

	----if a fast sulution is not found yet
	----its suitable to make it a cipher alogorithm
	----making Diffe-Hellman key swapping protacal

#=====================================================

chapter 2 ring

section 2.1 defination of ring:

	for tuple(R,+,*,0,1) of 5:
		R is set
		+, * is 2 operand operator on set R
		0, 1 in R
		having:
			R1(addational commu group)	: 
				(R,+,0) is a commutative group

			R2(multiply half group)		: 
				(R,*,1) is a half group (with unit 1)

			R3(mul distrubution to add)	: 
				for a,b,c in R:
					a*(b+c) == a*b + a*c

		def Ring R ( noted as (R,+,*,0,1) )


explaination of Ring:		
	+,* is namely add and multiply 
	1 is ring unit
	0 is ring zero unit
	for a in ring (R,+,*,0,1):
		a''*a == 1, name a'' as reverse unit
		a""+a == a, name a"" as negative unit

	varients:
	(1)
			(R,+,0) is a addational (default) group of Ring, having G1,G2,G3
			(R,*,1) is a multiply half group of Ring, having G1,G2


	(2)

		R4(multiply commutative half group):
			(R,*,1) has G1,G2,G4 making commu half group

		for Ring in Rings:
			(R,+,*,0,1) has R4 
			----meaning (R,*,1) has G1,G2,G4 making a comm half group
		
		def commutaitve ring R

	(3)
		R5(entity law): (R*,*,1) is a group (ring with G3 reverse ) 

		for Ring in Rings:
			(R,+,*,0,1) has R5
			for a in R*:
				exist. a'' ,a''* a == 1

			----where R* == R-{0} (the ring still uses R rather than R*)
			----meaning (R*,*,1) has G1,G2,G3 making a group
		
		def entity

	(4)
		R6(field law):(R*,*,1) is a commu group

		for Ring in Rings:
			(R,+,*,0,1) has R5 (certainly has R5)
			----R* == R-{0} (the ring still uses R rather than R*)
			----meaning (R*,*,1) has G1,G2,G3,G4 making a commu group

		def field


#===============================================
section 2.2 instances of rings

instances of rings:
	(1) int Ring

	(Z,+,*,0,1): 
		Z is the set R
		(Z,+,0) is a commu group (with add unit 0,and inverse)
		(Z,*,1) is a commu half group (with unit 1 without inverse)
		for a,b,c in Z:
			a*(b+c) == a*b + a*c

	making 	(Z,+,*,0,1) a ring	(noted as ring Z)

	(2) rational number field 
	
	(Q,+,*,0,1):
		Q is the set R
		(Q,+,0) is a commu group (with add unit 0,and inverse) ----G1,G2,G3,G4
		(Q,*,1) is a commu half group (with unit 1)			----G1,G2,G4
		
		R5 (Q*,*,1) is a commu group (with unit 1 without inverse) ----G1,G2,G3,G4
		
		R3:
		for a,b,c in Z:
			a*(b+c) == a*b + a*c

	making 	(Q,+,*,0,1) a field	(noted as field Q)		

#=====================================================
section 2.3 complete ring and 0 factor

defination of complete Ring:
	(1) defination of 0 factor:
		for a,b in Ring:
			a != 0, b != 0
			a*b == 0

		def a,b 0 factor of Ring

	(2)comlete ring:
		for a,b in commu ring R:
			a*b != 0

		def complete Ring
			----no 0 factor

		eg. tuple(Z26, +mod 26, *mod 26, 0, 1) 	

#======================================================

section 2.4 idea

defination of idea:
	I is subgroup of Ring R:
	for a in I:
		for r in R:
			a*r in I
			r*a in I

	def I idea of R 

principal idea:
	I is idea of commu ring R:
		I={r*a|r in R} where a in I

	def I principal idea of ring R(noted as I=(a) )


idea instance:
	for int ring (Z,+,*,0,1):
		nZ={...-2n, -1n, 0, 1n, 2n ...}

	( noted as nZ=(n) )	
	nZ is idea of Ring Z as well as  principal idea of Ring Z

#=====================================================================
#

section 2.5 polynomial on Ring (polynomial with coffecient in Ring)

defination:
	for x in letters:
		
		a[i] in Ring R	
		n in Z
			
		def  R[x] ={ f(x)= (0~n)Sigma a[i]*x^i }

		explaination:
			a[i]*x^i is i-th item where a[i] is coffiecient
			a[n]*x^n is head item where Order(f(x)) == n
			if a[n] == 1 :
				f(x) called prime 1 polynomial
			exception:
				0 is a polynomial whose Order(0) is -infinite



section 2.6 operation of poly on Ring:
	
		for x in letters:
			a[i],b[j] in Ring R	
			n in Z
			
			f(x)= (0~n)Sigma a[i]*x^i
			g(x)= (0~m)Sigma b[j]*x^j


			def f(x) + g(x) == 	 (0~max(m,n)) Sigma ( a[k]+b[k] )*x^k

			def f(x) * g(x) == 	 (0~m)Sigma{(0~n)Sigma( a[i]*b[j] )*x^ i+j }


defination of polynomial Ring:
	first we define poly on Ring
	second those Rings totally make a Ring
	
	(R[x],+,*,0,1):			
		R[x] polynomial on Ring R (poly with coffiecient in Ring)
		+, * as defined above
		0 is the zero poly whose order is -infinite
		1 is the 1 poly with a int 1

	 	R1 (R[x],+,0) has G1,G2,G3
	 	R2 (R[x],*,1) has G1,G2
	 	R3 (mul distrubute over add)  h(x)*(g(x)+f(x)) == h(x)*g(x) + h(x)*f(x)


instances of polynomial Ring:
	(1) Q is rational number field 
		R is real number field

		Q[x] is rational polynomial ring 
		R[x] is real number poly ring

	(2) (Z26[x],+mod 26,*mod 26,0,1)  


complete Ring:
		for complete Ring in Rings:
			Order(f(x)*g(x)) == Order(f(x)) + Order(g(x))
			Order(f(x)+g(x)) == max(Order(f(x)) , Order(g(x)))



#=========================================================================

chapter 3 field

section 3.1 defination of field
	field was defined above in ring extension
	here is a independent defination of field

	for tuple(F,+,*,0,1):
		R1 (F,+,0) is a commu group
		R2 (F*,*,1) is a commu group
		R3 (mul distru over add) 

	def field (noted as  field (F,+,*,0,1) )
	

	+, * add and mul on field
	1 is unit of F
	0 is zero unit of F
	a'' (making 0) is addative inverse
	a"" (making 1) is multiply inverse

	substraction:
		def - == +(a'')

	division:
		def / == *(a"")

instances of fields:
	eg.1 field defined on Q ---- field Q == (Q,+,*,0,1)
	eg.2 field defined on R ---- field R == (R,+,*,0,1) 
	eg.3 field defined on C ---- field C == (C,+,*,0,1)


Galois filed:
	finite fields are called Galois field
		----noted as GF(q) if the filed has q elements

	
	eg. of Galois field
	GF(2) defined on F2={0,1}
	GF(2) == (F2,+ mod 2,* mod 2,0,1) (while more practiced operation is XOR )


field basic operation:
	(1)addative counter-cancel (use add inverse):
		for a,b,c in field F:
			if a+c == b+c:
				a==b
	
	(2)multiply counter-cancel (use mul inverse):
		for a,b,c in field F:
			if a*c == b*c where c!= 0:
				a == b		

	(3)inverse of add inverse:
		for a in field F:
			-(-a) == a 				

	(4)inveres of mul inverse:
		for a in field F:
			(a^-1)^-1 == a where a!=0

	(5)zero unit:
		for a in field f:
			a*0 == 0

	(6)field is a complete ring				
		for a,b in field F:
			if a*b == 0:
				a==0 or b==0

	(7) add, mul, add inverse, mul inverse are counter-penetrating 


#=============================================
#

sectioin 3.3 divison with a remainder

	for f(x),g(x) in F[x]:
		f(x)==q(x)*g(x) + r(x) where Order(r(x)) < Order(g(x))

	def r(x) remainder
	def g(x) diviser
	def f(x) devidee

	if r(x)==0:
		def g(x) factor of f(x) (noted as g(x)|f(x))	


defination of common diviser
	for f(x),g(x),q(x) in F[x]:
		
		if q(x)|f(x) and q(x)|g(x):
			def q(x) common divisor of g(x) and f(x)

		for q(x) in all common divisers:
			if q(x) has highest Order and is prime 1 poly:
				def q(x) greatest common diviser GCD (noted as (f(x),g(x)))

		if (f(x),g(x)) == 1:
			def f(x), g(x) are counter-primed



defination of common multiple
	for f(x),g(x),q(x) in F[x]:
		
		if f(x)|q(x) and g(x)|q(x):
			def q(x) common multiple of g(x) and f(x)

		for q(x) in all common divisers:
			if q(x) has lowest Order and is prime 1 poly:
				def q(x) smallest common multiple (noted as [f(x),g(x)])

#============================================================
#

section 3.4 polynomial on field

Euclid theorey on field:
	for f(x),f(x),q(x),r(x) in F[x]:
		f(x)==q(x)*g(x) + r(x) where Order(r(x)) < Order(g(x))
		
		(f(x),g(x)) == (g(x),r(x))

Euclid algorithm: 
	----represent GCD as linear combination of themselves
	for f(x),g(x) in F[x]:
		f(x),g(x) != 0
		exist.a(x),b(x):
			(f(x),g(x)) == a(x)*f(x) + b(x)*g(x)

#===============================================================

section 3.5 reduced polynomial
	for f(x) in F[x]:
		if f(x) has only constant factor c or cf(x):
			def reduced poly f(x) on field F

	eg.1

	 f(x)=x^2 - 2 
	 	is reduced in rational field Q
	 	not reduced in real field R 	----(x-root2)(x+root2)		

	eg.2 	

	f(x)=x^2 + 1
		is reduced in rational field Q
		is reduced in real field R
		not reduced in complex field C 	----(x-j)(x+j)



numeric basic theorey:
	for f(x) in F[x]:
		if Order(f(x)) >=1:
			it must be decomposed
			the decomposion is unique

root of reduced poly:
	for a in letters:
		if f(a) == 0 :
		def root a of f(x)

#==================================================================

section 3.6 congruence of polynomials:


congruence of polynomial:

	for f(x),g(x),m(x) in F[x]:
		f(x)==q(x)*m(x) + r(x) where Order(r(x)) < Order(m(x))
		g(x)==p(x)*m(x) + r(x) where Order(r(x)) < Order(m(x))

	def congruence f(x) == g(x) mod m(x)
	

pre-theorey:
	if f(x) == g(x) mod m(x):
		m(x) | f(x) - g(x)


operations of congruence:
	(1) self-congruence: 
			f(x) == f(x) mod m(x)

	(2)symmetrical:
			f(x) == g(x) mod m(x) <=> g(x)==f(x) mod m(x) 

	(3)transcendent:
			f(x) == g(x) mod m(x)
			g(x) == h(x) mod m(x)
			==>
			f(x)==h(x) mod m(x)

	(4)additivity:
			f(x) == g(x) mod m(x)
			p(x) == q(x) mod m(x)
			==>
			f(x)+p(x) == g(x)+q(x) mod m(x)

	(5)multiply:
			f(x) == g(x) mod m(x)
			p(x) == q(x) mod m(x)
			==>
			f(x)*p(x) == g(x)*q(x) mod m(x)
					
			
#==============================================================
#

section 3.7 residue class
	F[x] are polynomials defined on F:
	
	for f(x) in F[x]:
		for n-th reduced poly g(x) in F[x]:
			if f(x)/g(x) remain r(x) where Order(r(x))<=Order(g(x))

		def residue {f(x) |having common r(x)} (noted as F[x][p(x)])

	the defined field F has q elements and there will be q^n remainder

#===========================================================

section 3.8 subfield and hyperfield	

	for f(x),g(x) in F[x][p(x)]:
		def +:
			f(x)+g(x) == (f(x)+g(x))[p(x)]
		def *:
			f(x)*g(x) == (f(x)*g(x))[p(x)]
			
	if field F ,which is F[x] defined on, has q elements
		F[x][p(x)] has q^n elements
		tuple(F[x][p(x)], +mod p(x), *mod p(x), 0, 1) makes a field GF(q^n)

	F is subfield of F[x][p(x)]
	F[x][p(x)] is hyperfield of p(x) 



section 3.10 data array and polynomial:
	
	for f(x) in F[x] defined on GF(2):
		for A data array defined on GF(2):
			f(x)==a[n-1]x^n-1 ...a[1]x +a[0]
			A == (a[n-1]...a[1], a[0])

	def map A <-> f(x)


#=======================================================
#
chapter 4 about information security

section 4.1 introduction

	error correcting code
	pseudo random sequence
	classic cipher
	AES cipher
	elliptic curve cipher

#===========================================================
section 4.2 applications in AES

add and mul in AES:
	AES use reduced modules poly m(x)=x^8 + x^4 + x^3 + x +1 based on GF(2)
	F[x][m(x)] making GF(2^8)
	Byte add and mul is poly add&mul mod m(x) based on GF(2)

xtime(t) in AES:
	def xtime(t):
		t*f(x) mod m(x)=x^8 + x^4 + x^3 + x + 1
	
	----left shift and mod

#============================================================
section 4.3 elliptic curve cipher introduction:
	

Weierstrass equation:
	y^2 + a[1]xy + a[3] y == x^3 + a[3]x^2 + a[4]x +a[6]
	where a[i] is defined on field K
   
basic idea:

for K in fields:
	a[1],a[2],a[3],a[4],a[6] in K
	
	equation: y^2 + a[1]xy + a[3] y == x^3 + a[2]x^2 + a[4]x +a[6]a
	
	delta=-b[2]^2*b[8]-8b[4]^3-27b[6]^2+9b[2]*b[4]*b[6]
		
		where:b[2]=a[1]^2+4a[2]
			  b[4]=a[1]a[3]
			  b[]
			  b[]

	for delta!=0 in this curve equation:
		extract points from K
			 making set E:{(x,y)|y^2 + a[1]xy + a[3] y == x^3 + a[2]x^2 + a[4]x +a[6]} union {O}
				where O is a infinite far away poniter
		j(E)=(b[2]^2 - 24b[4])^3/delta

		making a Abelian add group(proven under this add the set is a commu group):
			for P,Q in set E:
				find line L  connecting P,  Q
				R'' is another point L intersects with the curve

				find kine L''connecting R'',O (? it find the x-Asis mirror ?) 	
				R is another point L'' intersects with the curve
			
			def add(P,Q) == R


			there is also a algebra way to compute point R for specific K field:
				elliptic curve on Real number R
				elliptic curve on Prime number Fp(p>3)


common practice:
	for k == limited field Fp (where p is a lagre prime):
		
		a,b in K
		equation: y^2== x^3 + a*x^2 + b
	 	delta == (4a^3+27b^2) mod p != 0

	 	making Ep(a.b)={(x,y)|on the curve} 
	 		for x in range(0~p-1):
	 			calculate x^3 + a*x^2 + b 
	 			if has mod p square root:
					calculate mod p square root y
 					add (x,y) into set

 		for P,Q in set Ep(a,b):
			def add(P,Q):
			P+O=P
			P=(x,y) ,add inverse -P=(x,-y)
			2P = P+P = -S where S is intersect of P line with the curve
			P(x1,y1),Q(x2,y2)
				P+Q=R(x3,y3)
				
				x3=lambda^3-x1-x2 		mod p
				y3=lambda*(x1-x3)-y1 	mod p
				
				where lambda==(y2-y1)/x2-x1 ,	P!=Q
							==(3x1^2+a)/2y1 ,	P==Q


ECC:
	Fp is a Galois field, p is a prime
	E is a elliptic curve on Fp
	P is a point on E ,having Order n
	D={0,1,2 ... n-1}

	steps:
		receiver:
		choose private key d in D through tuple(p,E,P,n)
		calculate public key Q=dP
		
		sender:
		plaintext M is encode as points on E
		choose random k in D ,using public key making cipher C=(C1,C2)=(kP,M+kQ)

		reveiver:
		decripte with private key d, plaintext M == C2-dC1


learn to use matlab

#==========================================================================
#
chapter 5 number theorem

study object: integer

problems of number theorem:
	square sum
	high power sum: fermat theorem
	prime number inifite:4K+1 form,other form
	sibling prime:neighboured odds being primes 3,5,7	11,13
	N^2+1 form prime:5,17,37,101,197,257,401...


number theorem and IS:
	classic cryptography, backpack alogorithm
	RSA cipher alogorithm
	EIGamal public key 
	Rabin public key


section 5.1
introduction: 
	on a int Ring, +,-,* are closed operation but / will produce result in real field
	thus,to define another / on int Ring, we have division with remainder

divison with remainder:
	for a,b in int Ring:
			b!=0
			exist.unique. q,r
			a=b*q+r, 0<=r<|b|

	def / operator on int Ring
	def q uncomplete quotient ()	
	def r min-non-negative remainder

exact division
	if remainder r==0:
		def b |a
	
	else:	
		def b!|a


section 5.2 successive divison 

successive divison		
	a =bq1+r1
	b =r1q2+r2
	r1=r2q3+r3
	.
	.
	.
	rn-2=rn-1 *qn   + rn
	rn-1=rn   *qn+1 + rn+1 ( rn+1 ==0 )

	successive divison and roll back


section 5.3 greatest common diviser GCD
	
co-prime :
	(a1,a2,a3,a4...an)=1	


GCD with division:
	if a==qb+r:
		(a,b)=(b,r)


section 5.4 construct of GCD

construct GCD of (a,b) by linear combination of a,b:
	for a,b in int Ring:
		a,b!=0
		exist.u, v
		au + bv == (a,b)

construct min-common-multiple
	[a,b] == a*b/(a,b)	



section 5.5 undetermined equation
	for x,y in int Ring:
		a1,a2,n are given
		a1,a2!=0 	
		a1*x+a2*y = n 
	
	def solution condition (a1,a2)|n	

		steps:
			find (a1,a2)
			roll back to make	a1*u  + a2*v  == (a,b)
			times a rate making a1*up + a2*vp == (a,b)p = n

section 5.6 backpack alogorithm

encription:

	 Public key Pk	(a0,a1,a2,a3...an)
	 plain text	M 	(m0,m1,m2,m3...mn) on {0,1}
	 cipher C=Pk*M 	Sigma(ai*mi) (is partial sum of Pk)

decription:
 	given pack size C and items a0~an:
 		find which items are in pack (mi=1) or not in pack (mi=0)

Two major problems:
	if {ai} not properly constructed, not easy to decription for receiver
	if {ai} be hyper-incremental, easy for receiver and attacker to decripte

better ways to be extended


section 5.7 congruence
	for a,b in int Ring:
		if a==b (mod m)

	def a,b congruence


charateristics of congruence:
	(1) if a==b (mod m):
			m|a-b

	(2)if a==b (mod m):
			a^n ==	b^n  (mod m) # power
			f(a)==	f(b) (mod m) # polynomials


	(3)if a==b (mod m):
		if p==q (mod m):		

			m*a+u*p == n*b+v*q (mod m) 	#linear combination
			ap==bq (mod m)				#product

	(4)if ac==bc (mod m)
		if (m,c)==d:
			a==b (mod m/d)				#canceling

	(5) if a==b (mod mi) for all mi in {mi}:
			a==b (mod [m1,m2,m3..mn])

	(6)root of congruence equation x==a (mod m)
			are {x|x=a+km ,k in Z ring}		

1st-power congruence equation
	
	for a,b,m in int Ring:
		a*x == b(mod m)	

	def congruence equation (x)
	def solution x0 satisfying the equation
		----different soulution means to be different mod m result, not just diff number


solution condition: (a,m)=d && d|b
		
		x0 particular solution
		x==x0 + mt/d  t={0,1,2...d-1} (total d solutions)	
			if (a,m)=1 ax==1(mod m) has one solution x0 to be inverse of a (mod m)

	steps:
		(1)	find x0:
			find (a,m)==d
			roll back and represent d==ua+vm
			times a rate and get b == pd == pu*a+pv*m
			under mod m ,gets b==pu*a (mod m)
		x0 == pu mod m

		(2) fill in x.
	
section 5.9 backpack cipher 2

	receiver:
		(a0,a1...an)	as hyper pack items
	
		choose m:	m>a1+a2+a3...an
		choose u:	(u,m) =1
		
		u,m 			as private key
		
		bi=u*ai(mod m) 	
		(b0,b1...bn) 	as normal pack items ----public key

	sender:
		M=(m0,m1...mn)	as plaintext
		S=Sigma(mi*bi)	as cipher

	receiver:
		solve w: uw==1 mod m
		calculate (sw)0	min-non-negative remainder of sw mod m
			sw==(sw)0 (mod m) where 0<(sw)0<m

		transfer normal pack into hyper pack:
			sw==Sigma(mi*w*bi)==Sigma(mi*u*w*ai)==Sigma(mi*ai) (mod m)	


	for attacker: solve items{bi} and S 		----normal backpack
	for receiver: solve items{ai} and (sw)0		----hyper backpack



section 5.10 integer unique decomposion

prime charateristics:
	(1)
		for p in primes:
			for a in int:
				p|a or (a,p)=1

	(2)		
		for p in primes:
			if p|ab:
				p|a or p|b

integer unique decomposion:
	for a in integer
		a>1
		a=p1*p2*p3...pn	

	def standard decomposion a=p1^a1 * p2^a2 ... pn^an

section 5.11 residue system and residue class

definations:
	(1)
	for m in int:
		for r in range(0-m-1)
			m>0
			Cr={a|a=r+qm, q in Z}

	def Cr of mod m 

	there are m residue class for each different value of m

	(2)
	for Cr in all residue class {Cr}
		extract one number from Cr as ar
	
	making a0,a1...am-1
	
	def complete residue system

	
	(3)
	if ar<m:
	def min-non-negative residue system	

	(4)
	if (r,m)==1:
		Cr is co-primed residue class
	def co-primed residue clas Cr where (r,m)=1

	(5) 
	for Cr in co-primed residue class {Cr}
		extract one number from Cr as ar
	
	def reduced residue system


section 5.12 Euler function
	
Euler function:
	fai(n)
	given n 
	if n==1:
		fai(1)=1
	elif n==2:
		fai(2)=1
	elif	
		for i in range(0~n-1):
			if (i,n)==1: # 0 not co-prime to anything # 1 is co-primed to anything 
			fai(n)++;

charateristics of Euler function:
	(1) for p in primes:
			fai(p)=p-1

	(2) for m in int:
			a reduced residue system of mod m has fai(m) elements

	(3)if (m1,m2)==1 :
			fai(m1,m2)=fai(m1)*fai(m2)

	(4)for p in primes:
			fai(p^l)=p^l-p^(l-1)  					

	combining (3)(4) and int decomposion, any int n, fai(n) is computable

	(5) fai(m)=m Pai*(1-1/pi)	where Pai* is sequence multiply


section 5.13 Euler theorem

Euler theorem
	if (a,m)==1:
		a^fai(m)  == 1(mod m)x
		a^fai(m)+1== a(mod m)


Fermat theorem (an special occasion of Euler theorem)
	for p in primes:
		a^p == a(mod p)

section 5.14 Sunzi theorem

Sunzi theorem
	congruence equations
		x==b1 (mod m1)
		x==b2 (mod m2)
		.
		x==bk (mod mk)

	for mi in each-other co-primed int {mi}
		m = m1*m2*m3...mn 	
		m = mi*Mi 
			where Mi is m leave out mi 
		M'i' *Mi == 1 (mod mi)
			solve congruence equation x*Mi==1(mod mi)
	
	def solution x=M'1'*M1*b1 + M'2'*M2*b2 ... M'n'*Mn*bn(mod m)

		the unique.solution is not really "unique". 
		its a residue class



section 5.15 RSA

	receiver:
		choose large prime p,q
		calculate n=pq , fai(n)=(p-1)(q-1)	

		choose random e: 1<e<fai(n) and (e,fai(n))==1

		calculate d: de==1(mod fai(n))  

		p,q,fai(n),d as private key
		n,e 		 as public key

	sender:
		m 				as plaintext
		c = m^e(mod n)	as encription (this is calculation not congruence)
			----fast power algorithm

	receiver:
		m = c^d(mod n) as decription
			----fast power algorithm



section 5.15 prime

prime are infinite

	if primes are finite : p1,p2,p2...pn:
		let P=p1*p2...pn +1
		P is not a prime
		for p in primes p|P
			p|P-p1*p2...pn
			p|1
		contraction
	

prime counts
	lim[x->finite] pi(x)/(x/lnx) =1
	where pi(x) is prime counts
		  x/lnx as an approximation to pi(x)

section	 5.18

mersens prime
	a^n-1 is mersense number

	for A in mersense number: 
		if A=(a^n) -1 is a prime
			a==2 and n is a prime 


section 5.19 prime judgement

prime judegement
	(1)divison judegement
		for q in range(1,sqrt(p))
			if q is a prime:
				 q !| n

	(2)willson judegement
		 (p-1)! === -1 (mod p)

	(3)Lehmer judegement
		p-1 =Pai(pi^ai) as decomposion
		for pi in p-1 decomposion:
			ai^((p-1)/pi) != 1 (mod p)
			ai^(p-1) == 1(mod p)

	(4)Proth judgement
		p-1=mq 
			where q is a odd prime and 2q+1 > sqrt(p)

		if a^(p-1) == 1(mod p)
		   a^m 	!= 1(mod p)

		   	 		


