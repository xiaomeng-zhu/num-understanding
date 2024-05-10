"""
This file converts the original qqa dataset to prompts with instructions.
"""
import json
import pandas as pd


splits = ["train", "dev", "test"]
for split in splits:
    results = []
    with open(f"qqa_data/QQA_{split}.json", 'r') as file:
        data = json.loads(file.read())
    for d in data:
        question = d["question"]
        option1 = d["Option1"]
        option2 = d["Option2"]
        correct = d["answer"]
        formatted = f"<s> [INST] Answer this question given two options: {question} Option 1: {option1}. Option 2: {option2} [/INST] {correct} </s>"
        results.append(formatted)
    print(len(results))
    df = pd.DataFrame(results, columns = ["text"])
    df.to_csv(f'qqa_instruct/QQA_{split}_instruct.csv', index=False)