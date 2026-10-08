from dataclasses import dataclass

from app.tools.base import AssistantTool


@dataclass(frozen=True)
class IntentResult:
    intent: str
    tool_name: str | None
    confidence: float


class IntentClassifier:
    """Lightweight deterministic classifier used before LLM fallback."""

    def __init__(self, tools: list[AssistantTool]):
        self.tools = tools

    def classify(self, text: str) -> IntentResult:
        for tool in self.tools:
            if tool.can_handle(text):
                return IntentResult(
                    intent=tool.name,
                    tool_name=tool.name,
                    confidence=1.0,
                )

        return IntentResult(
            intent="unknown",
            tool_name=None,
            confidence=0.0,
        )
