# Classe Retângulo com método calcular_area
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area_retangulo(self):
        return self.largura * self.altura

# Classe Círculo com método calcular_area
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area_circulo(self):
        return 3.14 * self.raio * self.raio

# Adaptador para permitir que ambos os objetos sejam usados de maneira consistente
class AdaptadorCirculo:
    def __init__(self, circulo):
        self.circulo = circulo

    def calcular_area(self):
        return self.circulo.calcular_area_circulo()

# Função que recebe um objeto com um método "calcular_area"
def calcular_area_objeto(objeto):
    return objeto.calcular_area()

# Exemplo de uso
retangulo = Retangulo(5, 10)
circulo = Circulo(4)

# Chamada direta aos métodos de cálculo de área
print("Área do retângulo:", retangulo.calcular_area_retangulo())
print("Área do círculo:", circulo.calcular_area_circulo())

# Usando o adaptador para calcular a área do círculo
adaptador_circulo = AdaptadorCirculo(circulo)
print("Área do círculo com adaptador:", calcular_area_objeto(adaptador_circulo))
