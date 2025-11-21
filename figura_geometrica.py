# Clase base para cualquier figura
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    #Método general para el área (base * altura)
        return self.ancho * self.alto

   #Método que las clases hijas deben sobrescribir
    def perimetro(self):
        raise NotImplementedError()

   # Muestra los valores de la figura

    def __str__(self):
        return f"[Figura: {self.ancho} x {self.alto}]"