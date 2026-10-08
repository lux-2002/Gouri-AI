from datetime import datetime

from app.tools.base import AssistantTool


class TimeTool(AssistantTool):
    @property
    def name(self) -> str:
        return "time"

    def can_handle(self, text: str) -> bool:
        normalized = text.lower()
        return "what time" in normalized or "current time" in normalized or normalized == "time"

    def execute(self, text: str) -> str:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."


class ExitTool(AssistantTool):
    @property
    def name(self) -> str:
        return "exit"

    def can_handle(self, text: str) -> bool:
        normalized = text.lower().strip()
        return normalized in {"exit", "quit", "goodbye", "stop", "bye"}

    def execute(self, text: str) -> str:
        return "Goodbye! Have a great day."
