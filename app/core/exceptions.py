class AssistantError(Exception):
    """Base exception for assistant-specific failures."""


class ToolExecutionError(AssistantError):
    """Raised when a tool cannot complete its requested action."""


class LLMConfigurationError(AssistantError):
    """Raised when the LLM is requested but incorrectly configured."""
