# Sem o padrão "Bridge"

# Classes para tipos de mídia
class MusicPlayer:
    def play(self, platform):
        if platform == "Windows":
            print("Reproduzindo música no Windows.")
        elif platform == "MacOS":
            print("Reproduzindo música no macOS.")
        elif platform == "Android":
          print("Reproduzindo música no Android")
        elif platform == "IOS":
          print("Reproduzindo música no IOS")
          
        

class VideoPlayer:
    def play(self, platform):
        if platform == "Windows":
            print("Reproduzindo vídeo no Windows.")
        elif platform == "MacOS":
            print("Reproduzindo vídeo no macOS.")
        elif platform == "Android":
            print("Reproduzindo vídeo no Android")
        elif platform == "IOS":
            print("Reproduzindo vídeo no IOS")

music_player = MusicPlayer()
video_player = VideoPlayer()

op_system = input("Digite o seu sistema operacional: ")

music_player.play(op_system)
video_player.play(op_system)
