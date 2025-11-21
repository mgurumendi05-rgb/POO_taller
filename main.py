 from cuadrado import Cuadrado
from rectangulo import Rectangulo
from datetime import datetime

def sumar_areas(figuras):
    total = 0
    for fig in figuras:
        total += fig.area()
    return total

def sumar_perimetros(figuras):
    total = 0
    for fig in figuras:
        total += fig.perimetro()
    return total

def main():
    print("Fecha y hora:", datetime.now())
    print("----FIGURAS----- ")
    # Creación
    c1 = Cuadrado(4)
    c2 = Cuadrado(2)
    r1 = Rectangulo(3, 6)
    r2 = Rectangulo(5, 2)

    figuras = [c1, c2, r1, r2]

    # Mostrar valores
    for f in figuras:
        print(f, "| Área:", f.area(), "| Perímetro:", f.perimetro())

    print("\n--- Probando validación ---")
    try:
        Cuadrado(-5)
    except ValueError as e:
        print("Error atrapado:", e)

    print("\n--- Totales ---")
    print("Total áreas:", sumar_areas(figuras))
    print("Total perímetros:", sumar_perimetros(figuras))

if __name__ == "__main__":
   main()
