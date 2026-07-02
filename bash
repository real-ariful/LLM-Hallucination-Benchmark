#!/bin/bash

# Create project structure
mkdir -p llm-hallucination-benchmark/{src,data,reports,notebooks,tests}
cd llm-hallucination-benchmark

# Create README.md
cat > README.md << 'EOF'
# LLM Hallucination Benchmark

A comprehensive benchmarking tool for evaluating and comparing hallucination rates across multiple Large Language Models (LLMs).

## 🎯 Overview

This tool systematically evaluates LLMs on factual questions to measure and compare hallucination rates. It supports both local models (via Hugging Face Transformers) and API-based models (via OpenAI-compatible APIs).

## ✨ Features

- **Multi-Model Support**: Compare GPT, Qwen, DeepSeek, Llama, and more
- **Hallucination Detection**: Measures factual accuracy and hallucination rates
- **Flexible Backends**: Support for both local models and API endpoints
- **Comprehensive Reporting**: Export CSV reports and visualization dashboards
- **Prompt Injection Testing**: Includes robust prompt injection detection
- **Extensible Architecture**: Easy to add new models and evaluation metrics

## 🛠️ Tech Stack

- Python 3.9+
- Hugging Face Transformers
- OpenAI-compatible APIs
- Pandas for data analysis
- Jupyter for interactive development
- Matplotlib/Seaborn for visualization

## 📦 Installation

### Prerequisites

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-hallucination-benchmark.git
cd llm-hallucination-benchmark

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
