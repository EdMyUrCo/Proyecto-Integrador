def laberinto(dimension, muros):
    laberinto = []
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            if tuple([i, j]) in muros:
                fila.append('#')
            else:
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
    imprimir_laberinto = laberinto(6, muro)

    # Mostrar el laberinto por pantalla
    for i in imprimir_laberinto:
        print(''.join(i))

if __name__ == "__main__":
    main()
