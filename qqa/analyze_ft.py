import csv, json
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

DIRECTION_MAPPING = {'weight_strongness': "positive", 
                     'volume_velocity': "negative", 
                     'distance_size': "negative", 
                     'time_resistance': "positive", 
                     'distance_time': "positive", 
                     'velocity_distance': "positive", 
                     'temperature_resistance': "positive", 
                     'velocity_time': "negative", 
                     'thickness_strongness': "positive", 
                     'weight_gravity': "positive", 
                     'energy_distance': "negative", 
                     'time_distance': "positive", 
                     'punch_strongness': "positive", 
                     'distance_brightness': "negative", 
                     'velocity_velocity': "positive", 
                     'friction force_distance': "negative", 
                     'velocity_temperature': "positive", 
                     'distance_temperature': "negative", 
                     'velocity_resistance': "negative", 
                     'distance_resistance': "negative", 
                     'weight_acceleration': "negative", 
                     'weight_thickness': "positive"
                     }

def read_response(filename):
    results = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            results.append(row[0])
    results = results[1:]
    return results


def read_gold(filename):
    gold_list = []
    with open(filename) as file:
        qqa_data = json.loads(file.read())
    for g in qqa_data:
        gold = {}
        gold["correct_index"] = g["answer"]
        if g["answer"] == "Option 1":
            gold["correct_text"] = g["Option1"]
        elif g["answer"] == "Option 2":
            gold["correct_text"] = g["Option2"]
        gold_list.append(gold)
    return gold_list


def get_response_base(full, manual):
    responses = [i.split("[/INST]")[1] for i in full]
    chosen = []
    for i, r in enumerate(responses):
        first_sent = r.split(".")[0]
        if "option 2 is the correct answer" in r.lower() or "the correct answer is option 2" in r.lower() or "the answer is option 2" in r.lower():
            chosen.append("Option 2")
        elif "option 1 is the correct answer" in r.lower() or "the correct answer is option 1" in r.lower() or "the answer is option 1" in r.lower():
            chosen.append("Option 1")
        elif "option 2" in first_sent.lower():
            # print(i, first_sent, 2)
            chosen.append("Option 2")
        elif "option 1" in first_sent.lower():
            # print(i, first_sent, 1)
            chosen.append("Option 1")
        else:
            current_manual = [m for m in manual if m["index"] == str(i)]
            assert len(current_manual) == 1
            chosen_correctness = current_manual[0]["model_index"]
            gold = current_manual[0]["correct_index"]
            if chosen_correctness == str(-1) or chosen_correctness == str(0): # if answer incorrectly
                if gold == "Option 1":
                    chosen.append("Option 2")
                else:
                    chosen.append("Option 1")
            else: # if answer correctly
                chosen.append(gold)
            
            # print(i, r)
    return responses, chosen

def get_response_ft(full):
    responses = [i.split("[/INST]")[1] for i in full]
    chosen = []
    for i, r in enumerate(responses):
        chosen.append(r.split(".")[0].split(":")[0].strip())
    return responses, chosen

def prepare_manual_annotation(gold, results, chosen):
    assert len(gold) == len(results)
    assert len(results) == len(chosen)
    manuals = []
    for i in range(len(gold)):
        if chosen[i] == 0:
            manuals.append([i, gold[i]["correct_text"], gold[i]["correct_index"], results[i]])
    manuals_df = pd.DataFrame(manuals, columns=["index", "correct_text", "correct_index", "results"])
    manuals_df.to_csv("manuals.csv", index=False)

def get_manual_annotation(fn):
    rows = []
    with open(fn, 'r') as file:
        csv_reader = csv.DictReader(file)
        rows = [row for row in csv_reader]
    return rows

def get_labels(annotated):
    givens = [a["given_unit"] for a in annotated]
    answers = [a["answer_unit"] for a in annotated]

    # populate correlation field
    for a in annotated:
        a["correlation"] = DIRECTION_MAPPING[(a["given_unit"] + "_" + a["answer_unit"])]
                                             
    correlations = [a["correlation"] for a in annotated]
    same_unit = [a["given_unit_same"] for a in annotated]
    return givens, answers, correlations, same_unit

def get_scores(gold_response, model_response):
    gold_chosen = [g["correct_index"] for g in gold_response]
    f1 = f1_score(gold_chosen, model_response, average="micro")
    precision = precision_score(gold_chosen, model_response, average="micro")
    recall = recall_score(gold_chosen, model_response, average="micro")
    scores = {
        "f1":f1,
        "precision":precision,
        "recall":recall
    }
    return scores

def get_accuracy(gold_response, model_response):
    # return a list of 0 or 1
    accuracies = []
    for a, b in list(zip(gold_response, model_response)):
        if a["correct_index"] == b:
            accuracies.append(1)
        else:
            # print(a,b)
            accuracies.append(0)
    return accuracies

if __name__=="__main__":

    base_results_full = read_response("results/QQA_test_instruct_response_base.csv")
    ft_results_full = read_response("results/QQA_test_instruct_response_ft.csv")
    gold = read_gold("dataset/QQA_test.json")

    # for some items whose response is hard to judge from the string, we manually annotated the correctness
    manual = get_manual_annotation("results/accuracy_annotated.csv")
    
    category_manual = get_manual_annotation("results/QQA_test_instruct_annotated.csv")
    givens, answers, correlations, same_unit = get_labels(category_manual)

    base_responses, base_chosen = get_response_base(base_results_full, manual)
    base_responses_df = pd.DataFrame(base_responses)
    base_responses_df.to_csv("results/cleaned_results/base_responses.csv")

    ft_responses, ft_chosen = get_response_ft(ft_results_full)
    ft_responses_df = pd.DataFrame(ft_responses)
    ft_responses_df.to_csv("results/cleaned_results/ft_responses.csv")

    ft_scores = get_scores(gold, ft_chosen)
    base_scores = get_scores(gold, base_chosen)

    ft_accuracy = get_accuracy(gold, ft_chosen)
    base_accuracy = get_accuracy(gold, base_chosen)
    result_df = pd.DataFrame(list(zip(givens, answers, correlations, same_unit, base_accuracy, ft_accuracy)),
                            columns = ["given_unit", "answer_unit", "correlation", "same_unit", "base_accuracy", "ft_accuracy"])
    # prepare the dataframe so that it is easier for significance analysis in R
    result_df.to_csv("results/cleaned_results/base_vs_ft_result.csv", index=False)