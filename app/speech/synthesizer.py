import pyttsx3

from app.utils.logger import get_logger


class SpeechSynthesizer:
    """Converts text responses into speech using one persistent engine."""

    def __init__(self):
        self.logger = get_logger(__name__)
        self.engine = pyttsx3.init()

    def speak(self, text: str) -> None:
        if not text:
            return

        self.logger.info("Speaking response.")
        self.engine.say(text)
        self.engine.runAndWait()
