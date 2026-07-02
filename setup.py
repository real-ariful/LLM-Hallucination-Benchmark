from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
long_description = fh.read()

setup(
name="llm-hallucination-benchmark",
version="0.1.0",
author="AZM Ariful Haque Real",
author_email="azmarifulhaque@gmail.com",
description="A benchmarking tool for evaluating LLM hallucination rates",
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/yourusername/llm-hallucination-benchmark",
packages=find_packages(where="src"),
package_dir={"": "src"},
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
"Topic :: Scientific/Engineering :: Artificial Intelligence",
],
python_requires=">=3.9",
install_requires=[
"torch>=2.0.0",
"transformers>=4.30.0",
"accelerate>=0.20.0",
"openai>=1.0.0",
"pandas>=2.0.0",
"numpy>=1.24.0",
"matplotlib>=3.7.0",
"seaborn>=0.12.0",
"sentence-transformers>=2.2.0",
"jupyter>=1.0.0",
"tqdm>=4.65.0",
"python-dotenv>=1.0.0",
],
entry_points={
"console_scripts": [
"hallucination-benchmark=src.cli:main",
],
},
)
