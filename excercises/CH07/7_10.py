"""
7-10
Dream Vacation: Write a program that polls users about their dream vaca-
tion. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.

Jun 2025
@jmerort
"""
exit = False
destinos = []

while exit == False:
    destino = input("¿Si pudieses ir de vocaciones a cualquier lugar, a dónde irías? (Entra 'X' para salir): ")

    if destino != 'X' and destino != 'x':
        destinos.append(destino)
    else:
        exit = True

print("¡Fin de la encuesta!\nEstos son los destinos vacacionales preferidos por nuestros usuarios:")

for destino in destinos:
    print(f"\t-{destino}")

