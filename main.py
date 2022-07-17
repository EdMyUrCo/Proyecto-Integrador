import readchar

nombre = input("Digite tu nombre: ")

print("Bienvenid@ al proyecto", nombre)

status = True

while status:
    print("Ingrese caracter: ")
    c = readchar.readkey()
        
    if c == readchar.key.DOWN:
        status = False
    else:
        print("Ingrese caracter: ")
        c = readchar.readkey()
        