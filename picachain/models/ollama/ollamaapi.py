from typing import Any, List
import ollama as ol

class Ollama_Integration:
    
    def __init__(self, model: str = "llava", host: str = "http://localhost:11434") -> None:
        self.model = model
        self.host = host

    def completion(self, messages: List[dict[str, Any]]):
        response = ol.chat(model=self.model, messages=messages)
        return str(response['message']['content'])
    
    def stream_completion(self, messages: List[dict[str, Any]]):
        stream = ol.chat(model=self.model, messages=messages, stream=True)
        for chunk in stream:
            if not chunk['message']:
                continue
            yield str(chunk['message']['content'])

