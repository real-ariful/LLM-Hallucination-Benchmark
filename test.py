from src.benchmark import HallucinationBenchmark
from src.models import ModelFactory

# Initialize benchmark
benchmark = HallucinationBenchmark()

# Load models
models = ModelFactory.create_models([
    "gpt-4",
    "qwen-7b",
    "deepseek-v3",
    "llama-3"
])

# Run benchmark
results = benchmark.run(models, num_questions=100)

# Generate report
benchmark.export_report("reports/hallucination_report.csv")
benchmark.visualize("reports/visualization.png")
