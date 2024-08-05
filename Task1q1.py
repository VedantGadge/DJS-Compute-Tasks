name_list = ["Orion", "Barracuda", "Amethyst", "Blade", "Wasp", "Nemesis", "Fury", "Cobra", "Tempest", "Leo", "Scythe"]

def codename_generated():
    for i in range (len(name_list)):
        for j in range(i+1,len(name_list)):
            print(name_list[i],name_list[j],sep=' ')
    
codename_generated()