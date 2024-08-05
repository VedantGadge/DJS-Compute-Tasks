meetup_districts = {'III', 'VI', 'IV', 'V'}
patrolled_districts = ['I', 'II', 'XII', 'IX', 'XI', 'IV', 'II', 'VI']
setC = set(patrolled_districts)
new_meetup_districts = meetup_districts - setC
print('New Meet Up Districts:',new_meetup_districts)