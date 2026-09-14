"""
Configuration settings for the Style Finder application.
"""

# Groq model configuration
# Qwen 3.8 27B - multimodal model supporting text + image inputs
# Supports thinking/instruct modes, tool use, and JSON mode
GROQ_MODEL_ID = "qwen/qwen3.8-27b"

# Model parameters
MODEL_TEMPERATURE = 0.2
MODEL_TOP_P = 0.6
MODEL_MAX_TOKENS = 2000

# Image processing settings
IMAGE_SIZE = (224, 224)
NORMALIZATION_MEAN = [0.485, 0.456, 0.406]
NORMALIZATION_STD = [0.229, 0.224, 0.225]

# Default similarity threshold
SIMILARITY_THRESHOLD = 0.8

# Number of alternatives to return from search
DEFAULT_ALTERNATIVES_COUNT = 5
