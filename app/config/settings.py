from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


def _as_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    assistant_name: str = os.getenv("ASSISTANT_NAME", "Gouri")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    max_context_messages: int = int(os.getenv("MAX_CONTEXT_MESSAGES", "10"))

    music_directory: str = os.getenv("MUSIC_DIRECTORY", "")

    llm_enabled: bool = _as_bool(os.getenv("LLM_ENABLED"), False)
    llm_base_url: str = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "")

    speech_language: str = os.getenv("SPEECH_LANGUAGE", "en-US")
    listen_timeout: int = int(os.getenv("LISTEN_TIMEOUT", "5"))
    phrase_time_limit: int = int(os.getenv("PHRASE_TIME_LIMIT", "8"))
