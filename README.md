# Unpacking Large Language Model’s Performance on Quantitative Understanding: NumEval @ SemEval - 2024

This repository contains the code and datasets used in our research paper "Unpacking Large Language Model's Performance on Quantitative Understanding: NumEval @ SemEval - 2024". We evaluate state-of-the-art large language models (LLMs) on tasks that require quantitative understanding and reasoning. This work was submitted as part of the SemEval - 2024 challenges.

## Contents

- `QA_task.py`: Python script for the quantitative analysis tasks.
- `QNLI.ipynb`: Jupyter notebook for the Quantitative Natural Language Inference task.
- `QP.ipynb`: Jupyter notebook for the Quantitative Prediction task.
- `QQA Fine Tuning.ipynb`: Jupyter notebook for fine-tuning models on the Quantitative Question Answering task.
- `requirements.txt`: Required libraries to run the notebooks and scripts.

## Installation

To set up a local development environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/numeval-semeval-2024.git
   cd numeval-semeval-2024
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each notebook/script in this repository corresponds to a different part of our analysis:

- **Quantitative Analysis Tasks**: Run `python QA_task.py` to execute the analysis tasks described in our paper.
- **QNLI**: Use Jupyter to open `QNLI.ipynb` and run the cells to reproduce our NLI analysis.
- **QP**: Use Jupyter to open `QP.ipynb` and execute the quantitative predictions as detailed.
- **QQA Fine Tuning**: Open `QQA Fine Tuning.ipynb` in Jupyter to see our fine-tuning process for the QQA task.

## Contributing

Contributions to this project are welcome! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- Helen Zheng - helen.zheng@yale.edu
- Miranda Zhu - miranda.zhu@yale.edu

## Acknowledgments

- Yale University Department of Statistics and Data Science
- Yale University Department of Linguistics

---

This README template includes basic sections that most projects will need. Depending on the specifics of your project, you might want to include additional sections such as `Data`, `Results`, or `Citations` if you want to provide direct references to the datasets or key results from your paper.
