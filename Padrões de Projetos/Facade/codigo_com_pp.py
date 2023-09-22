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

class HomeTheaterFacade:
    def __init__(self, dvd, amp, tv):
        self.dvd = dvd
        self.amp = amp
        self.tv = tv

    def assistir_filme(self, movie):
        self.dvd.on()
        self.dvd.play(movie)

        self.amp.on()
        self.amp.set_surround_sound()

        self.tv.on()
        self.tv.set_input("DVD")

# Usando o padrão Facade para assistir um filme
def main():
    dvd = DVDPlayer()
    amp = Amplifier()
    tv = TV()

    home_theater = HomeTheaterFacade(dvd, amp, tv)
    home_theater.assistir_filme("O Senhor dos Anéis")

main()
