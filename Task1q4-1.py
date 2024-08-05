your_districts = ['I', 'IV', 'V', 'I', 'VI', 'IX', 'X', 'II', 'III', 'I']
their_districts = ['V', 'IV', 'VI', 'XII', 'VII', 'IV', 'VI', 'VIII', 'III']
setA = set(your_districts)
setB = set(their_districts)
meetup_districts = setA & setB
print("Meet Up Districts:",meetup_districts)