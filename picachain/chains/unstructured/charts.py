import os
from typing import Union

from PIL import Image

from picachain.chains.chain import Chain
from picachain.models.openai.openai import OpenAI_Model
from picachain.unstructured.charts import Chart, ChartParser


class ChartConversationChain(Chain):
    def __init__(self, chart: Union[Image.Image, os.PathLike]) -> None:
        super().__init__()
        self.chart = chart

    def get_chart_content(self):
        return str(ChartParser.from_image(self.chart).content)

    def run(self, query: str):
        self.llm = OpenAI_Model()
        self.chart_content = self.get_chart_content()
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
