class CalculadoraRaizCuadrada:
    def __init__(self):
        self.numero = 0.0
        self.raiz = 1.0

    def ingresar_datos(self):
        self.numero = float(input("Dame el valor de a: "))

    def calcular_raiz(self, iteraciones=10):
        for k in range(1, iteraciones + 1):
            self.raiz = (self.raiz + self.numero / self.raiz) / 2
            print(f"La raíz después de {k} iteraciones es {self.raiz}")

    def obtener_raiz(self):
        return self.raiz


# Ejemplo de uso
calculadora = CalculadoraRaizCuadrada()
calculadora.ingresar_datos()
calculadora.calcular_raiz()
