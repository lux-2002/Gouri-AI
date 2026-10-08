from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    role: str
    content: str


class ConversationContext:
    """Bounded in-memory conversation context."""

    def __init__(self, max_messages: int = 10):
        if max_messages < 1:
            raise ValueError("max_messages must be >= 1")
        self._messages = deque(maxlen=max_messages)

    def add(self, role: str, content: str) -> None:
        self._messages.append(Message(role=role, content=content))

    def messages(self) -> list[dict[str, str]]:
        return [
            {"role": message.role, "content": message.content}
            for message in self._messages
        ]

    def clear(self) -> None:
        self._messages.clear()

    def __len__(self) -> int:
        return len(self._messages)
