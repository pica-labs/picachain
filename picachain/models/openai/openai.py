from typing import Any, List


class OpenAI_Model:
    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        try:
            import openai
            from openai import OpenAI
        except ImportError:
            raise ImportError(
                "Failed to import openai. Install using `pip install openai`."
            )
        self.model = model
        try:
            self.client = OpenAI()
        except ValueError:
            raise ValueError("Failed to get OPENAI_API_KEY from environment.")

    def completion(self, messages: List[dict[str, Any]]) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return str(completion.choices[0].message.content)

    def stream_completion(self, messages: List[dict[str, Any]]):
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            if not chunk.choices:
                continue
            yield str(chunk.choices[0].delta.content)
