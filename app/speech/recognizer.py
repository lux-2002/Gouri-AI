import speech_recognition as sr

from app.config.settings import Settings
from app.utils.logger import get_logger


class SpeechRecognizer:
    """Converts microphone audio into text."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self.recognizer = sr.Recognizer()
        self.logger = get_logger(__name__)

    def listen(self) -> str:
        try:
            with sr.Microphone() as source:
                self.logger.info("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(
                    source,
                    timeout=self.settings.listen_timeout,
                    phrase_time_limit=self.settings.phrase_time_limit,
                )

            self.logger.info("Recognizing speech...")
            text = self.recognizer.recognize_google(
                audio,
                language=self.settings.speech_language,
            )

            text = text.strip()
            self.logger.info("Recognized input: %s", text)
            return text

        except sr.UnknownValueError:
            self.logger.warning("Speech could not be understood.")
            return ""

        except sr.RequestError as exc:
            self.logger.error("Speech recognition service error: %s", exc)
            return ""

        except (sr.WaitTimeoutError, TimeoutError):
            self.logger.warning("Listening timed out.")
            return ""

        except OSError as exc:
            self.logger.error("Microphone/audio device error: %s", exc)
            return ""
