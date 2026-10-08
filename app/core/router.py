from dataclasses import dataclass
from time import perf_counter

from app.ai.intent_classifier import IntentClassifier
from app.ai.response_generator import ResponseGenerator
from app.tools.base import AssistantTool
from app.utils.logger import get_logger


@dataclass(frozen=True)
class RouteResult:
    response: str
    intent: str
    tool_name: str | None
    latency_ms: float
    used_llm: bool


class IntentRouter:
    def __init__(
        self,
        tools: list[AssistantTool],
        classifier: IntentClassifier,
        response_generator: ResponseGenerator,
    ):
        self.tools = {tool.name: tool for tool in tools}
        self.classifier = classifier
        self.response_generator = response_generator
        self.logger = get_logger(__name__)

    def route(self, text: str) -> RouteResult:
        started = perf_counter()

        result = self.classifier.classify(text)

        if result.tool_name:
            tool = self.tools[result.tool_name]
            response = tool.execute(text)
            used_llm = False
        else:
            response = self.response_generator.generate(text)
            used_llm = True

        latency_ms = round((perf_counter() - started) * 1000, 2)

        self.logger.info(
            "route intent=%s tool=%s llm=%s latency_ms=%s",
            result.intent,
            result.tool_name,
            used_llm,
            latency_ms,
        )

        return RouteResult(
            response=response,
            intent=result.intent,
            tool_name=result.tool_name,
            latency_ms=latency_ms,
            used_llm=used_llm,
        )
