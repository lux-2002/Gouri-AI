from pathlib import Path
import os
import platform
import random

from app.tools.base import AssistantTool


class MusicTool(AssistantTool):
    def __init__(self, music_directory: str = ""):
        self.music_directory = Path(music_directory).expanduser() if music_directory else None

    @property
    def name(self) -> str:
        return "music"

    def can_handle(self, text: str) -> bool:
        return "play song" in text.lower() or "play music" in text.lower()

    def execute(self, text: str) -> str:
        if self.music_directory is None:
            return "Music playback is not configured. Set MUSIC_DIRECTORY in your environment."

        if not self.music_directory.exists():
            return "The configured music directory does not exist."

        supported = {".mp3", ".wav", ".m4a", ".aac", ".flac"}
        songs = [
            path for path in self.music_directory.iterdir()
            if path.is_file() and path.suffix.lower() in supported
        ]

        if not songs:
            return "No supported audio files were found in the configured music directory."

        selected = random.choice(songs)

        if platform.system() == "Windows":
            os.startfile(str(selected))
            return f"Playing {selected.stem}."

        # macOS/Linux fallback.
        if platform.system() == "Darwin":
            os.system(f'open "{selected}"')
        else:
            os.system(f'xdg-open "{selected}"')

        return f"Playing {selected.stem}."
