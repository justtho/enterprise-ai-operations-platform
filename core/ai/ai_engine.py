from core.ai.prompt_manager import PromptManager
from core.ai.model_provider import MockModelProvider


class AIEngine:
    """Shared AI Engine used by all enterprise AI capabilities."""

    def __init__(self):
        self.prompt_manager = PromptManager()
        self.model_provider = MockModelProvider()

    def summarize(self, text: str) -> str:
        prompt = self.prompt_manager.summarize_prompt(text)
        return self.model_provider.generate(prompt)

    def classify(self, text: str) -> str:
        prompt = self.prompt_manager.classify_prompt(text)
        return self.model_provider.generate(prompt)

    def extract(self, text: str) -> str:
        prompt = self.prompt_manager.extract_prompt(text)
        return self.model_provider.generate(prompt)

    def chat(self, question: str, context: str = "") -> str:
        prompt = self.prompt_manager.chat_prompt(question, context)
        return self.model_provider.generate(prompt)