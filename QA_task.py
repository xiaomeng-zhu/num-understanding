import sys
from transformers import AutoTokenizer, LlamaForCausalLM, LlamaTokenizer, AutoModelForCausalLM

MODEL = sys.argv[1]

if MODEL == "llama2":
    model_name = "meta-llama/Llama-2-7b-hf"
    tokenizer_name = "meta-llama/Llama-2-7b-hf"
elif MODEL == "llama3":
    model_name = None

tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """Given a question and two options, choose the option that best answers the question:

Example:
Question: The ranger and the rustler both were riding horses that galloped at the same speed.  The rustler left at 01:00 where as the ranger left at 0500 hours. Who has traveled further??
Option1: the ranger
Option2: the rustler
Answer: Option 2

Based on this example, answer the following question:
Question: Tina is racing her two dogs. Her greyhound weighs 40 kgs, and her rottweiler weighs 35 kgs. The dog that gets faster more quickly is the?
Option1: rottweiler
Option2: greyhound
"""
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
outputs = model.generate(input_ids, max_new_tokens=200)
print(tokenizer.decode(outputs[0]))
