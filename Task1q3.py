Aliens =  ['gunther', 'karzan', 'pip1do', 'jarzk', 'p0ppy', 'gunther', 'garzon ', 'marz4']
alien_prob={}

for alien in Aliens:
    if(any(char.isdigit() for char in alien)):
        alien_prob[alien]=100 
    elif(alien.startswith('g') and 'arz' in alien):
        alien_prob[alien]=75
    elif('arz' in alien):
        alien_prob[alien]=50
    else:
       alien_prob[alien]=25

print(alien_prob)