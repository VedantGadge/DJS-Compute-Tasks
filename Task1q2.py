register = ["Gunther", "karzan", "pip1do", "amelia", "emma", "jarzk", "P0ppy", "gunther", "Daisy"," Demelza ", "Lisa ", "garzon ", "marz4"]
humans = []
aliens = []
def identityChecker():
    for i in register:
        name = i.lower()
        if(name.startswith('g') or 'arz' in name or any(char.isdigit() for char in name)):
            aliens.append(name)
        else:
            humans.append(name)

identityChecker()
print('Humans = ',humans)
print('Aliens = ',aliens)
