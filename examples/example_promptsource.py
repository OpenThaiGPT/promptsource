# Load an example from the datasets ag_news
from datasets import load_dataset
dataset = load_dataset("ag_news", split="train")
example = dataset[1]

from promptsource.templates import DatasetTemplates
ag_news_prompts = DatasetTemplates('ag_news')

print("prompts.templates")
print(ag_news_prompts.templates)
print()

print("prompts.name_to_id_mapping")
print(ag_news_prompts.name_to_id_mapping)
print()

prompt = ag_news_prompts['classify_question_first']

# Apply the prompt to the example
result = prompt.apply(example)
print("INPUT: ", result[0])
print("TARGET: ", result[1])