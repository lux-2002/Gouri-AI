from app.ai.llm_client import LLMClient
from app.core.context import ConversationContext
from app.core.exceptions import LLMConfigurationError


class ResponseGenerator:
    """Generates responses for requests not handled by local tools."""

    SYSTEM_PROMPT = (
        "You are Gouri, a concise and helpful voice assistant. "
        "Answer naturally and keep spoken responses reasonably short."
    )

    def __init__(self, llm_client: LLMClient, context: ConversationContext):
        self.llm_client = llm_client
        self.context = context

    def generate(self, user_text: str) -> str:
        messages = [{"role": "system", "content": self.SYSTEM_PROMPT}]
        messages.extend(self.context.messages())
        messages.append({"role": "user", "content": user_text})

        try:
            return self.llm_client.generate(messages)
        except LLMConfigurationError:
            return (
                "I don't have an AI response engine configured for that request yet. "
                "You can enable the optional LLM integration in the environment settings."
            )
        except Exception:
            return "I couldn't reach the AI service right now. Please try again later."
