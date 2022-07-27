import os
os.system("clear")
import readchar

nombre = input("Digite tu nombre: ")

print("Bienvenid@ al proyecto", nombre)

# status = True

# while status:
#     print("Ingrese caracter: ")
#     c = readchar.readkey()
        
#     if c == readchar.key.DOWN:
#         status = False

for i in range (0, 50+1):
    print("Ingrese caracter: ")
    c = readchar.readkey()

    if c == readchar.key.CTRL_N:
        
