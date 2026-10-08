from app.ai.intent_classifier import IntentClassifier
from app.ai.llm_client import LLMClient
from app.ai.response_generator import ResponseGenerator
from app.config.settings import Settings
from app.core.context import ConversationContext
from app.core.router import IntentRouter
from app.speech.recognizer import SpeechRecognizer
from app.speech.synthesizer import SpeechSynthesizer
from app.tools.base import AssistantTool
from app.utils.logger import get_logger


class VoiceAssistant:
    def __init__(self, settings: Settings, tools: list[AssistantTool]):
        self.settings = settings
        self.logger = get_logger(__name__)

        self.speech = SpeechRecognizer(settings)
        self.synthesizer = SpeechSynthesizer()

        self.context = ConversationContext(settings.max_context_messages)
        self.llm_client = LLMClient(settings)
        self.response_generator = ResponseGenerator(
            self.llm_client,
            self.context,
        )

        self.classifier = IntentClassifier(tools)
        self.router = IntentRouter(
            tools=tools,
            classifier=self.classifier,
            response_generator=self.response_generator,
        )

    def run(self) -> None:
        self.synthesizer.speak(
            f"Hello! I am {self.settings.assistant_name}. How can I help you?"
        )

        while True:
            user_input = self.speech.listen()

            if not user_input:
                continue

            self.context.add("user", user_input)

            result = self.router.route(user_input)

            self.context.add("assistant", result.response)
            self.synthesizer.speak(result.response)

            if result.intent == "exit":
                break
