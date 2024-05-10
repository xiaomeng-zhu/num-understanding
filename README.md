# Unpacking Large Language Model’s Performance on Quantitative Understanding: NumEval @ SemEval - 2024

This repository contains the codes, instructions on downloading datasets, and enviornment requirements. We evaluate state-of-the-art large language models (LLMs) on tasks that require quantitative understanding and reasoning.

## Repository Structure

Within this repository, you will find the following files and directories:
  
  <!-- - [`QA_task.py`](https://github.com/xiaomeng-zhu/num-understanding/blob/main/QA_task.py): Python script for performing quantitative analysis tasks. -->
  - [`qqa`](https://github.com/xiaomeng-zhu/num-understanding/blob/main/qqa): Directory containing all materials for the Quantitative Question-Answering task.
      - `dataset`: Directory containing the original qqa dataset (also available on Google Drive specified in the next section).
      - `qqa_instruct`: The qqa dataset converted to instruction fine-tuning format.
      - `results`: Results for QQA from Experiment 1 and Experiment 2.
          - `cleaned_results`: Model responses with the prompt removed.
      - `analyze_ft.py`: Python script for analyzing Experiment 2 results.
      - `create_inst_dataset.py`: Python script for converting original dataset to instruction fine-tuning format.
      - `exp1_qqa_prompt.ipynb`: Jupyter notebook for prompting models for the Quantitative Question-Answering task.
      - `exp2_qqa_ift.ipynb`: Jupyter notebook for fine-tuning Llama 2 on QQA_train.json.
      - `significance_test.R`: R script for significance testing.
  - [`QNLI.ipynb`](https://github.com/xiaomeng-zhu/num-understanding/blob/main/QNLI.ipynb): Jupyter notebook for the Quantitative Natural Language Inference task.
  - [`QP.ipynb`](https://github.com/xiaomeng-zhu/num-understanding/blob/main/QP.ipynb): Jupyter notebook for the Quantitative Prediction task.
  <!-- - [`QQA Fine Tuning.ipynb`](https://github.com/xiaomeng-zhu/num-understanding/blob/main/QQA%20Fine%20Tuning.ipynb): Jupyter notebook detailing the fine-tuning process for the Quantitative Question Answering task. -->
  - [`requirements.txt`](https://github.com/xiaomeng-zhu/num-understanding/blob/main/requirements.txt): Contains all the necessary Python packages required to run the scripts and notebooks.

## Installation

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/xiaomeng-zhu/num-understanding.git
cd num-understanding
pip install -r requirements.txt
```

## Datasets

**Accessing the Datasets:**

All datasets are available for access and download via our Google Drive folder:
[Access Datasets Here](https://drive.google.com/drive/folders/10uQI2BZrtzaUejtdqNU9Sp1h0H9zhLUE)

Please refer to the individual notebooks for specific details on which dataset is used for each task.

1. **Quantitative Prediction (QP):** The **QP** task evaluates the model's ability to predict the magnitude of numerical values stated in text, requiring the identification and contextual understanding of numerical entities.

2. **Quantitative Natural Language Inference (QNLI):** **QNLI** involves determining if a hypothesis can logically be deduced from a premise, specifically focusing on quantitative content.

3. **Quantitative Question-Answering (QQA):** **QQA** challenges models to answer questions that involve arithmetic calculations or quantitative comparisons.

## Usage

To reproduce the analysis and results described in our paper:

- Run the following commands for QQA:
  ```bash
  cd qqa
  python analyze_ft.py
  ```
- Open and run the Jupyter notebooks (`QNLI.ipynb`, `QP.ipynb`, `exp1_qqa_prompt.ipynb`) to follow the methodologies used in each specific task.

## Contact

- Helen Zheng - helen.zheng@yale.edu
- Miranda Zhu - miranda.zhu@yale.edu

## Acknowledgments

- Yale University Department of Statistics and Data Science
- Yale University Department of Linguistics
