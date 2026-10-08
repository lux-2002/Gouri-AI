import requests

from app.config.settings import Settings
from app.core.exceptions import LLMConfigurationError
from app.utils.logger import get_logger


class LLMClient:
    """Small provider-agnostic OpenAI-compatible chat client."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = get_logger(__name__)

    @property
    def enabled(self) -> bool:
        return (
            self.settings.llm_enabled
            and bool(self.settings.llm_api_key)
            and bool(self.settings.llm_model)
        )

    def generate(self, messages: list[dict[str, str]]) -> str:
        if not self.enabled:
            raise LLMConfigurationError(
                "LLM fallback is disabled or missing API configuration."
            )

        url = self.settings.llm_base_url.rstrip("/") + "/chat/completions"

        payload = {
            "model": self.settings.llm_model,
            "messages": messages,
            "temperature": 0.4,
        }

        headers = {
            "Authorization": f"Bearer {self.settings.llm_api_key}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
