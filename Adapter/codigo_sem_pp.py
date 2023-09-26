# Classe Retângulo com método calcular_area
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Classe Círculo com método calcular_area
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio * self.raio

# Exemplo de uso
retangulo = Retangulo(5, 10)
circulo = Circulo(4)

# Chamada direta aos métodos de cálculo de área
print("Área do retângulo:", retangulo.calcular_area())
print("Área do círculo:", circulo.calcular_area())