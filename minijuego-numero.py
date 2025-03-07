import random
import os

def clear():
    sistema = os.name
    if sistema == "nt": # windows
        os.system("cls")
    else: #Linux / macOS
        os.system("clear")

def juego(num_max, record):
    num = random.randint(1, num_max)
    intentos= 0
    print("\033[1;32mIntenta adivinar el numero del 1 al", num_max, ":\033[0m] ")

    while True:
        try:
            num_usuario = int(input("Introduce tu número: "))
            intentos += 1
            if num_usuario > num :
                print("Prueba con un numero más \033[1;31mpequeño\033[0m]")
            elif num_usuario < num:
                print("Prueba con un número más \033[1;31mgrande\033[0m]")
            else:
                print("\033[1;32m¡Correcto! El total de intentos és:\033[0m] ", intentos)
                try:
                    with open(record, "r") as f:
                        record_actual = int(f.read().strip())
                except FileNotFoundError:
                    record_actual = float("inf")

                if intentos < record_actual:
                    print(f"¡Nuevo récord establecido! Récord anterior: {record_actual}")
                    with open(record, "w") as f:
                        f.write(str(intentos))
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

def mostrar_records():
    print("\033[1;32mRécords\033[0m] ")
    for rango, file in  [(10, "record10.txt"), (20, "record20.txt"), (100, "record100.txt")]:
        try:
            with open(file, "r") as f:
                record = f.read().strip()
            print(f"Récord actual [1-{rango}]: {record}")
        except FileNotFoundError:
            print(f"Récord actual [1-{rango}]: No disponible")


def main():
    clear()
    while True:
        print("\033[1;32mElige una opcion:\033[0m] ")
        print("1- Nueva Partida")
        print("2- Récords")
        print("3- Salir")
        opcion = input("\033[1;32mElige una opción (1-3):\033[0m] ")

        if opcion == "1":
            clear()
            print("a- 1-10")
            print("b- 1-20")
            print("c- 1-100")
            opcion1 = input("\033[1;32mElige una opción (a-b-c):\033[0m] ")
            
            if opcion1 == "a":
                juego(10, "record10.txt")
            elif opcion1 == "b":
                juego(20, "record20.txt")
            elif opcion1 == "c":
                juego(100, "record100.txt")
        elif opcion == "2":
            mostrar_records()
        elif opcion == "3": # Reescribir los archivos 
            clear()
            with open("record10.txt", "w") as f:
                f.write("100")
            with open("record20.txt", "w") as f:
                f.write("100")
            with open("record100.txt", "w") as f:
                f.write("100")
            print("\033[1;31mSaliendo del juego...\033[0m]")
            break
        else:
            print("Opció no válida")
main()