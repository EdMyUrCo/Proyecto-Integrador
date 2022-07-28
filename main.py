import os


import readchar

nombre = input("Digite tu nombre: ")

print("Bienvenid@ al proyecto", nombre)

status = True
cont = 0

while status and cont < 50:
    
    print("Ingrese caracter: ")
    c = readchar.readkey()
        
    if c == readchar.key.DOWN:
        status = False
    
    if c == "n":
        cont += 1
    
    os.system('cls' if os.name == 'nt' else 'clear')
        
