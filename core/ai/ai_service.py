from abc import ABC, abstractmethod


class AIService(ABC):
    """Shared AI service interface used by all platform modules."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class MockAIService(AIService):
    """Temporary AI service for Sprint 2 before Bedrock integration."""

    def generate(self, prompt: str) -> str:
        return (
            "AI response placeholder.\n\n"
            "In the next sprint, this will connect to Amazon Bedrock."
        )