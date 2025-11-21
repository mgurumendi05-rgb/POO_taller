from figura_geometrica import FiguraGeometrica

# Un rectángulo también es una figura geométrica
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto) # Llama al constructor de la clase base

    # Perímetro del rectángulo
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    # Mostrar la info del rectángulo
    def __str__(self):
        return f"Rectangulo(ancho={self.ancho}, alto={self.alto})"