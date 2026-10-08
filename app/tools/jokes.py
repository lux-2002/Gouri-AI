import pyjokes

from app.tools.base import AssistantTool


class JokeTool(AssistantTool):
    @property
    def name(self) -> str:
        return "joke"

    def can_handle(self, text: str) -> bool:
        return "joke" in text.lower()

    def execute(self, text: str) -> str:
        return pyjokes.get_joke(language="en", category="neutral")
