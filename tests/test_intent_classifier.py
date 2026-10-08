from app.ai.intent_classifier import IntentClassifier
from app.tools.system import TimeTool


def test_time_intent():
    classifier = IntentClassifier([TimeTool()])

    result = classifier.classify("What is the current time?")

    assert result.intent == "time"
    assert result.tool_name == "time"
    assert result.confidence == 1.0


def test_unknown_intent():
    classifier = IntentClassifier([TimeTool()])

    result = classifier.classify("Explain machine learning")

    assert result.intent == "unknown"
    assert result.tool_name is None
