# Style Finder

Style Finder is a small Gradio application for analyzing fashion images. Users can upload an outfit image, or choose one of the included examples, and the app returns a catalog-style fashion analysis with visually similar item details.

## What It Does

The app combines image embeddings, similarity search, and a vision language model:

- Encodes uploaded images with a pretrained ResNet50 model.
- Compares the uploaded image against precomputed embeddings in `swift-style-embeddings.pkl`.
- Finds the closest matching outfit and related items from the dataset.
- Sends the uploaded image and matched item details to IBM watsonx using the configured Llama vision model.
- Displays a formatted fashion analysis in the Gradio interface.

## Project Structure

```text
app.py                         Main Gradio application
config.py                      Model, region, and image processing settings
models/image_processor.py      Image encoding and similarity matching
models/llm_service.py          IBM watsonx / Llama vision model integration
utils/helpers.py               Response formatting and dataset helpers
examples/                      Sample images for the UI
swift-style-embeddings.pkl     Precomputed fashion image embeddings dataset
requirements.txt               Python dependencies
```

## Getting Started

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

By default, the Gradio app launches on:

```text
http://127.0.0.1:5000
```

## Configuration

Core settings live in `config.py`, including the IBM watsonx model ID, project ID, region, image size, normalization values, and similarity threshold.

The app requires access to IBM watsonx AI for the Llama vision response generation. Make sure your environment is authenticated before running the application.
