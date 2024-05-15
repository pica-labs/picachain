---
sidebar-poisition: 1
---

# Chroma DB 

Setting up chroma DB to use for storing image embeddings for semantic search and image retrieval. 

## Getting started

Install dependencies before we get started.
```bash
pip install -U picachain 
```

## Prepare images

To get started, we need a set of images that will act as our knowledgebase which we are going to push on the vector database. 

**Images for Search**

```python
# list of images
from PIL import Image
images = [Image.open('img1.png'), Image.open('img2.png')]
```

**Query image**
```python
img = Image.open("img.png")
plt.imshow(img)
```
![image](https://github.com/pica-labs/picachain/assets/136924835/ca9f4fcd-3001-42d0-863d-9aa86fd61fb5)



## Import dependencies

```python
# import dependencies
from picachain.chains.image.search import ImageSearchChain
from picachain.datastore import ChromaStore
from picachain.embedding import ClipEmbedding
from picachain.retriever import ImageRetriever 
```

## Create vectorstore 

Picachain makes it easy to initiate a vector store index in chormadb. 

```python
# initiate vectorstore
datastore = ChromaStore("test-collection")
```

## Prepare the CLIP Embedding

To create embeddings, we use **CLIP** model by **OpenAI**. To read more on CLIP model, check out openai's official [documentation](https://openai.com/index/clip).

```python
embedding = ClipEmbedding()
```

`ClipEmbedding` is responsible for vectorization of images. 

## Initiate Retriever

Now that our vectorstore and embedding is initiated, we build the Image retriever.

```python
retriever = ImageRetriever(datastore, embedding, images)
```

## Create Image Search Chain

Next step is to create an `ImageSearchChain` that takes a query image an retrieves `top_k` similar images from our vector store.

```python
img_chain = ImageSearchChain.from_image(retriever, embedding, img) # img is query image
result = img_chain.similar_images(top_k=3) # retrive top 3 images
```

**Plot the images**
```python
import matplotlib.pyplot as plt

num_images = len(result)
fig, axes = plt.subplots(1, num_images, figsize=(12, 4))

for i, (img, score) in enumerate(result):
    axes[i].imshow(img)
    axes[i].set_title(f'Score: {score}')
    axes[i].axis('off')
plt.tight_layout()
plt.show()
```
![image](https://github.com/pica-labs/picachain/assets/136924835/8e2abbff-00c0-4b54-ba29-426e7b43d5e7)





