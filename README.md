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

![image](https://github.com/pica-labs/picachain/assets/136924835/57c400e7-3615-4775-b3aa-c2c211307ef0)
*Fig: Image Search Engine Overview*

```python
# initiate embedding, datastore and retriever
embedding = ClipEmbedding()
datastore = ChromaStore("test-collection")
retriever = ImageRetriever(datastore, embedding, images)
image_search = ImageSearch(retriever, embedding, img)
result = image_search.search_relevant_images(top_k=3) # get top 3 relevant images

## Output 
# [(img, score), (img, score)]
```
### Conversation with Charts/Graphs

Create a conversation chain and ask questions from chart/graph images.

![image](https://github.com/pica-labs/picachain/assets/136924835/a30c6969-98ee-43ac-beed-5425487aa95b)
*Fig: Conversation chain for Q&A with charts/graphs*


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

