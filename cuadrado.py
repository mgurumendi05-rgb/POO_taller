from figura_geometrica import FiguraGeometrica

# Un cuadrado es una figura geométrica
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado) # Como un cuadrado tiene ambos lados iguales, los mandamos dos veces

    def area(self):
        return self.ancho ** 2

    def perimetro(self):
        return 4 * self.ancho

    # Mostrar la info del cuadrado
    def __str__(self):
        return f"[Cuadrado lado={self.ancho}]"
