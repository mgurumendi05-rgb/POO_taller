Este taller aplica programación orientada a objetos usando encapsulamiento, herencia, polimorfismo, setters, getters, y sobrescritura de métodos.
El taller incluye tres clases principales: FiguraGeometrica, Cuadrado y Rectangulo.
Además, se implementa un programa principal que prueba áreas, perímetros y validaciones.

La clase base FiguraGeometrica controla el ancho y el alto con setters que validan que los valores sean mayores que cero. Además incluye un método de área y deja el perímetro para que lo implementen las clases hijas.

Las clases Cuadrado y Rectangulo heredan de la clase base. Cada una define su propio perímetro, su área y la forma en la que se muestra al imprimir el objeto.

En el archivo main.py se crean distintas figuras, se muestran sus áreas y perímetros, se prueba un valor inválido y se demuestran las funciones que suman áreas y perímetros de manera polimórfica.

El repositorio debe incluir la ejecución del programa junto con la captura donde se vea la fecha, la hora y los resultados obtenidos.
