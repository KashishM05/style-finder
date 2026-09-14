# Migration from IBM WatsonX to LangChain + Groq

This document describes the migration from IBM WatsonX AI to LangChain + Groq for the Style Finder application.

## Overview

The application has been migrated from the paid IBM WatsonX AI infrastructure to a **completely free** setup using Groq's API with LangChain as the orchestration framework.

### Why This Change?
- **Cost**: Groq offers a generous free tier (500K tokens/day, no credit card required)
- **Speed**: Groq's LPU hardware delivers 500+ tokens/sec
- **Flexibility**: LangChain provides a unified interface, making future provider switches trivial
- **Vision Support**: Groq's Llama 4 Scout model supports multimodal (image + text) inputs

---

## Files Changed

### 1. `requirements.txt`

**Removed:**
```
ibm-watsonx-ai==1.1.20
google-search-results==2.4.2
```

**Added:**
```
langchain>=0.3.0
langchain-core>=0.3.0
langchain-groq>=0.2.0
python-dotenv>=1.0.0
```

### 2. `config.py`

**Removed:**
```python
LLAMA_MODEL_ID = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8"
PROJECT_ID = "skills-network"
REGION = "us-south"
```

**Added:**
```python
GROQ_MODEL_ID = "qwen/qwen3.8-27b"
MODEL_TEMPERATURE = 0.2
MODEL_TOP_P = 0.6
MODEL_MAX_TOKENS = 2000
```

### 3. `.env.example`

**Changed from:**
```
IBM_API_KEY=your_ibm_api_key_here
```

**Changed to:**
```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. `models/llm_service.py`

Complete rewrite of the `LlamaVisionService` class:

**Removed:**
- IBM WatsonX SDK imports (`ibm_watsonx_ai`)
- IBM Credentials and APIClient setup
- IBM ModelInference wrapper

**Added:**
- LangChain imports (`langchain_groq`, `langchain_core.messages`)
- ChatGroq model initialization
- HumanMessage with multimodal content support

**Key Changes:**
- API key now loaded from `GROQ_API_KEY` environment variable
- Uses LangChain's `ChatGroq` wrapper for clean integration
- Multimodal messages use LangChain's `HumanMessage` format
- Constructor signature simplified (removed `project_id`, `region` params)

### 5. `app.py`

**Added:**
```python
from dotenv import load_dotenv
load_dotenv()
```

**Changed LlamaVisionService initialization:**
```python
# Before
self.llm_service = LlamaVisionService(
    model_id=config.LLAMA_MODEL_ID,
    project_id=config.PROJECT_ID,
    region=config.REGION
)

# After
self.llm_service = LlamaVisionService(
    model_id=config.GROQ_MODEL_ID,
    temperature=config.MODEL_TEMPERATURE,
    top_p=config.MODEL_TOP_P,
    max_tokens=config.MODEL_MAX_TOKENS
)
```

---

## Setup Instructions

### 1. Get a Free Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key

### 2. Configure Environment

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your Groq API key
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

---

## Groq Free Tier Limits

| Resource | Limit |
|----------|-------|
| Requests per minute | ~30 |
| Tokens per day | 500,000 |
| Max image size | 20 MB |
| Credit card required | No |

---

## Architecture Comparison

### Before (IBM WatsonX)
```
app.py → LlamaVisionService → IBM WatsonX SDK → IBM Cloud (us-south.ml.cloud.ibm.com)
                                    ↓
                           Llama 4 Maverick model
```

### After (LangChain + Groq)
```
app.py → LlamaVisionService → LangChain ChatGroq → Groq API (api.groq.com)
                                    ↓
                           Qwen 3.8 27B model
```

---

## Unchanged Components

The following components remain unchanged:
- **Gradio Interface**: All UI elements and interactions preserved
- **Image Processing**: ResNet50-based encoding (PyTorch)
- **Similarity Matching**: Cosine similarity with scikit-learn
- **Dataset Handling**: Pickle file loading and DataFrame operations
- **Helper Utilities**: Response formatting and processing

---

## Troubleshooting

### "GROQ_API_KEY environment variable is not set"
- Ensure `.env` file exists in project root
- Verify the API key is correctly set in `.env`
- Make sure `python-dotenv` is installed

### Rate Limit Errors
- Groq free tier limits to ~30 requests/minute
- Wait a few seconds between rapid requests
- Consider upgrading to paid tier for higher limits

### Model Not Found
- Verify the model ID in `config.py` matches available Groq models
- Current model: `qwen/qwen3.8-27b` (Qwen 3.8 27B with vision support)
- Check [Groq's model documentation](https://console.groq.com/docs/models) for current model IDs
- Groq rotates vision model availability quarterly - verify at docs before deploying
