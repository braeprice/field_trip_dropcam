# Data Project Environment Setup

This repository uses a Conda environment that includes:

- [`cookiecutter`](https://cookiecutter.readthedocs.io/) – for creating project templates
- [`pandas`](https://pandas.pydata.org/) – for data analysis
- [`doit`](https://pydoit.org/) – for build automation and task execution
- [`opencv`](https://opencv.org/) – for image and video processing

## 🧪 Requirements

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/)

---

## 🔧 Create the Environment

You can create the environment in one of two ways:

### ✅ Option 1: Using the provided `environment.yml`

```bash
conda env create -f environment.yml
conda activate goprobruv