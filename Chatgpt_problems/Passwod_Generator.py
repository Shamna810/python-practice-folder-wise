import random 
character = "Sfgh532VGedgv54hbvf"
password = ""
for i in range(12):
    password+=random.choice(character)
print(password)    
