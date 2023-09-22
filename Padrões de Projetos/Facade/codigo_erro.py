class DVDPlayer:
    def on(self):
        print("DVD Player ligado")

    def play(self, movie):
        print(f"Reproduzindo {movie}")

class Amplifier:
    def on(self):
        print("Amplificador ligado")

    def set_surround_sound(self):
        print("Configurando som surround")

class TV:
    def on(self):
        print("TV ligada")

    def set_input(self, source):
        print(f"Selecionando a fonte de entrada para {source}")

# Usando os componentes sem o padrão Facade
def assistir_filme():
    dvd = DVDPlayer()
    amp = Amplifier()
    tv = TV()

    dvd.on()
    dvd.play("O Senhor dos Anéis")

    amp.on()
    amp.set_surround_sound()

    tv.on()
    tv.set_input("DVD")

assistir_filme()
