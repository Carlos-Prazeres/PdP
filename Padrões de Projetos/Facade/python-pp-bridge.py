# Com o padrão "Bridge"

# Abstrações
class Media:
    def __init__(self, platform):
        self.platform = platform

    def play(self):
        pass

class Music(Media):
    def play(self):
        print(f"Reproduzindo música no {self.platform.name}.")

class Video(Media):
    def play(self):
        print(f"Reproduzindo vídeo no {self.platform.name}.")

# Implementações
class Platform:
    def __init__(self, name):
        self.name = name

class WindowsPlatform(Platform):
    pass

class MacOSPlatform(Platform):
    pass

# Uso
windows_platform = WindowsPlatform("Windows")
macos_platform = MacOSPlatform("MacOS")

music = Music(windows_platform)
video = Video(macos_platform)

music.play()
video.play()
