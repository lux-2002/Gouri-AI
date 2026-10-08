from app.ai.intent_classifier import IntentClassifier
from app.ai.response_generator import ResponseGenerator
from app.config.settings import Settings
from app.core.context import ConversationContext
from app.core.router import IntentRouter
from app.tools.system import TimeTool


class FakeGenerator:
    def generate(self, text):
        return "AI response"


def test_router_uses_local_tool():
    tools = [TimeTool()]
    classifier = IntentClassifier(tools)

    router = IntentRouter(
        tools=tools,
        classifier=classifier,
        response_generator=FakeGenerator(),
    )

    result = router.route("what time is it")

    assert result.intent == "time"
    assert result.tool_name == "time"
    assert result.used_llm is False
    assert result.latency_ms >= 0


def test_router_falls_back_to_ai():
    tools = [TimeTool()]
    classifier = IntentClassifier(tools)

    router = IntentRouter(
        tools=tools,
        classifier=classifier,
        response_generator=FakeGenerator(),
    )

    result = router.route("explain artificial intelligence")

    assert result.intent == "unknown"
    assert result.tool_name is None
    assert result.used_llm is True
    assert result.response == "AI response"
