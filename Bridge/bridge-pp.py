from __future__ import annotations
from abc import ABC, abstractmethod

# Abstração
class MediaPlayer:
    def __init__(self, platform: Platform) -> None:
        self.platform = platform

    def play(self) -> str:
        return (f"MediaPlayer: Playing media on platform:\n"
                f"{self.platform.play_media()}")


class AdvancedMediaPlayer(MediaPlayer):
    def play(self) -> str:
        return (f"AdvancedMediaPlayer: Advanced media playback on platform:\n"
                f"{self.platform.play_media()}")


# Implementação
class Platform(ABC):
    @abstractmethod
    def play_media(self) -> str:
        pass


class WindowsPlatform(Platform):
    def play_media(self) -> str:
        return "Playing media on Windows platform."


class MacOSPlatform(Platform):
    def play_media(self) -> str:
        return "Playing media on MacOS platform."


def client_code(media_player: MediaPlayer) -> None:
    # ...

    print(media_player.play(), end="")

    # ...


if __name__ == "__main__":
    # ...

    platform = WindowsPlatform()
    media_player = MediaPlayer(platform)
    client_code(media_player)

    print("\n")

    platform = MacOSPlatform()
    media_player = AdvancedMediaPlayer(platform)
    client_code(media_player)
