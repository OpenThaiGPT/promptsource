from promptsource.templates import DatasetTemplates, Template

dataset_name = "mmlu"
template_name = "QA01"

text_jinja = """Answer the following question:
{{question}} |||
{{ choices[answer] }}"""

answer_choices = '{{choices | join("|||")}}'
reference = ""

choices_in_prompt = True
languages = ["en"]
metrics = ["Accuracy"]
original_task = True

ds_temp = DatasetTemplates(dataset_name)
template = Template(template_name, "", "")
ds_temp.add_template(template)

template.metadata.choices_in_prompt = choices_in_prompt
template.metadata.languages = languages
template.metadata.metrics = metrics
template.metadata.original_task = original_task

ds_temp.update_template(
    current_template_name=template_name,
    new_template_name=template_name,
    jinja=text_jinja,
    reference=reference,
    metadata=template.metadata,
    answer_choices=answer_choices,
)
