from core.ai.ai_engine import AIEngine


class EmailIntelligenceService:
    """Business service for Email Intelligence capability."""

    def __init__(self):
        self.ai_engine = AIEngine()

    def summarize_email(self, email_text: str) -> str:
        return self.ai_engine.summarize(email_text)

    def classify_email(self, email_text: str) -> str:
        return self.ai_engine.classify(email_text)

    def extract_email_details(self, email_text: str) -> str:
        return self.ai_engine.extract(email_text)