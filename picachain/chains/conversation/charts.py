import os
from typing import List, Union

from PIL import Image

from picachain.chains.base import Chain
from picachain.models.openai.openai import OpenAI_Model
from picachain.structures import Document
from picachain.unstructured.charts import Chart, ChartParser


class ChartConversationChain(Chain):
    def __init__(self, charts: List[Document], llm: Union[OpenAI_Model]) -> None:
        super().__init__()
        self.charts = charts
        self.llm = llm

    def run(self, query: str):
        self.chart_content = "\n".join([doc.content for doc in self.charts])
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful data analyst, skilled in analyzing data from charts and answering complex questions from given data. Try to answer the question with short and concise answer.",
            },
            {
                "role": "system",
                "content": "DATA:",
            },
            {
                "role": "user",
                "content": self.chart_content,
            },
            {
                "role": "system",
                "content": "QUESTION:",
            },
            {"role": "user", "content": query},
            {
                "role": "system",
                "content": "ANSWER:",
            },
        ]
        response = self.llm.completion(self.messages)

        return str(response)
