# ✨ Multimodal Style Finder Application

> 📸 Upload a fit. Get the details. Look sharp. 👔

Style Finder is a fashion analysis app that identifies clothing items from images and matches them to a curated catalog. Powered by computer vision and a multimodal LLM, it turns any outfit photo into actionable style intel.

## How It Works

```
Your Image → ResNet50 → Similarity Search → Qwen Vision → Styled Results
```

1. **🖼️ Encode** - ResNet50 converts your image into a feature vector
2. **🎯 Match** - Cosine similarity finds the closest outfit in the dataset
3. **👁️ Analyze** - Qwen 3.8 27B vision model describes colors, patterns, materials, and style
4. **✨ Display** - Gradio serves up a clean, formatted breakdown with item links

## 🛠️ Tech Stack

| Layer | Tech |
|-------|------|
| **UI** | Gradio 5.x |
| **Vision Model** | Qwen 3.8 27B via Groq (free tier) |
| **LLM Framework** | LangChain |
| **Image Embeddings** | PyTorch + ResNet50 |
| **Similarity** | scikit-learn cosine similarity |

## Quick Start

```bash
# 1. Clone and enter
git clone <repo-url> && cd style-finder

# 2. Install deps
pip install -r requirements.txt

# 3. Get your free Groq API key at https://console.groq.com
cp .env.example .env
# Edit .env → add your GROQ_API_KEY

# 4. Run
python app.py
```

🌐 App launches at `http://127.0.0.1:5000` with a shareable public link.

## Project Structure

```
app.py                     Gradio app + orchestration
config.py                  Model config + thresholds
models/
  ├── llm_service.py       LangChain + Groq integration
  └── image_processor.py   ResNet50 encoding + matching
utils/helpers.py           Response formatting
examples/                  Sample images
swift-style-embeddings.pkl Pre-computed fashion embeddings
```

## Configuration

All tunables in `config.py`:

```python
GROQ_MODEL_ID = "qwen/qwen3.8-27b"  # Vision-capable multimodal model
MODEL_TEMPERATURE = 0.2             # Lower = more focused
MODEL_MAX_TOKENS = 2000             # Response length cap
SIMILARITY_THRESHOLD = 0.8          # Match confidence cutoff
```

## Why It's Free

Groq's free tier gives you:
- 500K tokens/day
- ~30 requests/minute  
- No credit card required
- Blazing fast LPU inference (500+ tokens/sec)