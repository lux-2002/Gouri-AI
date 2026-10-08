from abc import ABC, abstractmethod


class AssistantTool(ABC):
    """Contract for capabilities exposed to the assistant."""

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def can_handle(self, text: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def execute(self, text: str) -> str:
        raise NotImplementedError
