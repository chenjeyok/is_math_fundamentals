class introduction:

	3 math hard problems:
		(1)large integer discompose:no practical algorithms
			----computational security
			----RSA foundation
		(2)dircret logrithm problems:
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
		---- SxS->S ,(x,y)->z

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

		G3(inverse law)			: for a in set G:
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
			for key M is matrix Lm(Z[26]):
				(y1,y2,y3...ym) = (x1,x2,x3...xm)*M mod 26

		decription:
			for key M is matrix Lm(Z[26]):
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
				(R,*,1) is a half group (with unit)

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