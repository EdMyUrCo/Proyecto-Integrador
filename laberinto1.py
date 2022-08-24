def laberinto(dimension, muros):
    # Creamos una lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle iterativo para añadir las filas del laberinto.
    # i toma valores de 0 a dimension-1
    for i in range(dimension):
        # Creamos una lista vacía para añadir las casillas de la fila.
        fila = []
        # Bucle iterativo para recorrer las columnas del laberinto.
        # j toma valores de 0 a dimension-1.
        for j in range(dimension):
            # Condicional para comprobar si la tupla está en el la lista de muros.
            if tuple([i, j]) in muros:
                # Si la tupla está en la lista de muros ponemos una X en la casilla.
                fila.append('#')
            else:
                # Si la tupla no está en el muro ponemos un espacio en blanco en la casilla.
                fila.append('.')
        laberinto.append(fila)
    return laberinto

def main():
    # Tupla de coordenadas de las celdas con muro en el laberinto
    muro = ((0, 2), (0, 3), (0, 4),
            (1, 1), (1, 5),
            (2, 3), (2, 5),
            (3, 2), (3, 3), (3, 5),
            (4, 1), (4, 2), (4, 3), (4, 5),
            (5, 0), (5, 1), (5, 5))
    lab = laberinto(6, muro)

    # Mostrar el laberinto por pantalla
    for i in lab:
        print(''.join(i))

if __name__ == "__main__":
    main()
