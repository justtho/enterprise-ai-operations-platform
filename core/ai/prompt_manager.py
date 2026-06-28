class PromptManager:
    """Creates reusable prompts for AI capabilities."""

    def summarize_prompt(self, text: str) -> str:
        return f"""
        Summarize the following content clearly and professionally:

        {text}
        """

    def classify_prompt(self, text: str) -> str:
        return f"""
        Classify the following content into a meaningful business category:

        {text}
        """

    def extract_prompt(self, text: str) -> str:
        return f"""
        Extract key information, entities, and important details from the following content:

        {text}
        """

    def chat_prompt(self, question: str, context: str = "") -> str:
        return f"""
        Answer the question using the provided context.

        Context:
        {context}

        Question:
        {question}
        """