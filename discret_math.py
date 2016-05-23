discret_math
#=========================================
chapter 1 proposition logic

content of this chpater:
	basic ideas,knowledge and methods of proposition logic
	proposition logic is also named proposition arithmetic
		object: 		proposition
		study target:	relation between premise and conclusion

	(1)proposion and proposional conjunction
	(2)propositional formula
	(3)equivalent calculation
	(4)proposion normal form
	(5)tautology
	(6)conjunction complete func set
	(7)proposion logic and resoning		



section 1.1 proposition

def 1.1 proposition is a statement which can be(may not yet) judged True or False

def 1.2 proposition can be only True or False as its Truth Value

def 1.3 proposition with determined Truth Value propositional constant

def 1.4	propositional variable represented by a,b,c...
		eg. 
			a:" 3 is a prime "
			b:" 1+1 is 3 "

def 1.5 conjunction combining two proposition: 
			not  !
			and  &&
			or   ||
			implication  -> 
			double implication  <->

Truth Table of double implication:
	a == b then a<->b is True
	a != b then a<->b is False


def 1.6 compound proposion: combining atomic proposion through conjunction

def 1.7 proposional formula
		(1)proposional constant and variable are formula
		
		(2)if A,B are propo formula:
				not A 
				A&&B 
				A||B 
				A->B 
				A<->B
			(by previllge sequence)
			are all prop formula

		recursive defination:
		(3)anything derived from (1)and(2) are propo formula

def 1.8	explaination: a Truth Assignment
		U is set of all propo variables a,b,c...
		t is an explaination: truth assignment of tuple(0,1,0,1...) mapping from U to {0,1}

def 1.9 propo formula A under truth assignment t: U->{0,1}
		(1)if A is a variable x, t(A)=t(x)
		(2)if A is a constant a, t(A)=True or False due to Truth Table
		(3)if t(A) == 0, t(!A)=0

def 1.10 for any truth assignment t:
			t(A) == 1 def tautology
			t(A) == 0 def contradiction
			t(A) has 1 or 0 satisfiable


use truth table to judge tautology/contradiction/satisfiable

def 1.11 for proposion formula:
			if a <->b  is a tautology:
				a<=>b


basic equivalent arithmetic
	(1)!(!A)	<=>		A
	(2)A&B 		<=>		B&A
	(3)A|B 		<=>		B|A
	
	distrubution:
	(4)A|(B&C)	<=>		(A|B)&(A|C)	
	(5)A&(B|C)	<=>		(A&B)|(A&B)
	
	D''Morgan theorey:
	(6)!(A&B)	<=>		!A|!B
	(7)!(A|B)	<=>		!A&!B

	power equivalent:
	(8)A&A 		<=>		A
	(9)A|A 		<=>		A 

	constants
	(10)A&0		<=>		0
	(11)A|0 	<=>		A 
	(12)A&1		<=> 	A
	(13)A|1 	<=>		1

	implication:
	(14) A->B 	<=> 	!A | B
	(15) A->B 	<=> 	!B->!A 

	double implication:
	(16)!(A<->B)<=>		(A<->!B)
	(17)(A<->B) <=>		(A->B)&(B->A)
	(18)(A<->B) <=>		(!A<->!B)

	paralogy:
	(19) (A->B)&(A->!B) <=> !A
	(20)A|!A 	<=>		1
	(21)A&!A 	<=>		0

	absorb law:
	(22)A&(A|B) <=>		A
	(23)A|(A&B) <=>		A


application of basic equivalent formula	

def 1.12 limited proposition formula:
	for propo formula A:
		consist of propo variable/constant/conjunction !,&,|
	A is a limited propo formula

def 1.13 durity A*:
	for limited propo formula A:
		replace  with:
			& <----> |
			1 <----> 0
		
		noted as A*	

def 1.14 inner-deny A!:
	for limited propo formula A:
		replace  with:
			x<---->!x (atomic var x)
		
		noted as A!	

extended De Morgan throrem:
	(1) (!A)* 	<==>	!(A*)
	(2) (!A)!	<==>	!(A!)

	(3)practiacl 
		(A*)!	<==>	!A 
 


normal form for convience judging <=> relation:


def 1.15 propo variable and its deny are called charater
			simple conjuction consists of characters conjuncted
			simple disjunction consists of characters disjuncted


TH 1.7	simple disjunction is a tautology when it has a | !a
		simple conjunction is a paralogy when it has a & !a



def 1.16 normal form conjunction:
			simple disjunction being conjuncted

		 normal form disjunction:
			simple conjunction begin disjuncted


			
TH 1.9 normal form existance:
		for propo formaula A:
			exist.normal form disjunction A"" <==> A
			exist.normal form conjunction A'' <==> A
			
			




