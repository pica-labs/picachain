<div align="center">
<img src="https://github.com/d1pankarmedhi/picachain/assets/136924835/3a299c21-6590-4ee1-a3c1-73a92653f21e" height=150></img>
<h3>⚡️ Build quick LLM pipelines for all your image specific tasks</h3>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![PyPi license](https://badgen.net/pypi/license/pip/)]() [![PyPI version fury.io](https://badge.fury.io/py/picachain.svg)](https://pypi.python.org/pypi/picachain/)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/picachain.svg?style=social&label=Follow%20%40Picachain)](https://twitter.com/picachain)



</div>


**Picachain** is a framework for building complex non language pipelines for your LLM application. Build pipelines for your images, charts and graphs, parse, extract and generate using opensource models with ease, thanks to support for huggingface and diffusion libraries.

## 🌉 Things you can build with Picachain
- **Image Search Engines**: Build quick search engines for your images using ChromaDB and Pinecone for vector storage and retrieval. 
- **Image Generation**: Generate images with ease, thanks to support of Stable Diffusion, SDXL and SDXLturbo.
- **Chart Parsing**: Parse chart/graph from images and extract meaningful data and build a question-answering system on top of this using an LLM.

## 📌 Install Picachain

```bash
pip install picachain
```

## 🥇 Example Usage

### Build a quick image search engine

Use **ChromaDB** or **Pinecone** for storage with **CLIP** embeddings.
Check out a demo [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FbruIGMBrD7VW5jCHStHzGlsEuigbS0q?usp=sharing)


```python
from PIL import Image
import matplotlib.pyplot as plt

# import from picachain
from picachain.chains.image.search import ImageSearchChain
from picachain.datastore import ChromaStore, PineconeStore
from picachain.embedding import ClipEmbedding
from picachain.retriever import ImageRetriever
```

```python
img = Image.open("image.png") # query image
images = [...] # list of images
```

```python
# initiate embedding, datastore and retriever
embedding = ClipEmbedding()
datastore = ChromaStore("test-collection")
retriever = ImageRetriever(datastore, embedding, images)
img_chain = ImageSearchChain.from_image(retriever, embedding, img)
result = img_chain.similar_images(top_k=3)

for img, score in result: # [(img, score), (img, score)]
    plt.imshow(img)
    plt.show()

```

### Build Chart Conversation Chain

```python
from dotenv import load_dotenv
from picachain.chains.unstructured.charts import ChartConversationChain
from picachain.models.openai.openai import OpenAI_Model
load_dotenv()
```
```pyhton
chart_conv_chain = ChartConversationChain(
    chart="/home/home/dev/picachain/data/chart1.png", llm=OpenAI_Model()
)
response = chart_conv_chain.run(query="What do I eat?")
print(response)
```

## 💡 Contributing
As an open-source project, we are open to all kinds of contribution, be it through code, documentation, issues, bugs, or even feature suggestions. 

Feel free to check out [Contribution](/CONTRIBUTION.md) guide for more details.

## 🔧 Dependencies
We use poetry as the package manager. Make sure to refer to `pyproject.toml` for more details on dependencies. 

```bash
cd picachain
pip install poetry
poetry install 
```

