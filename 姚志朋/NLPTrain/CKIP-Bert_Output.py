####CKIP-Bert範例程式輸出
from transformers import TextClassificationPipeline
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from transformers import AutoTokenizer

Model_Location="./results/checkpoint-15/"

new_model = AutoModelForSequenceClassification.from_pretrained(Model_Location,output_attentions=True)
tokenizer = AutoTokenizer.from_pretrained(Model_Location)
# PipelineInterface = TextClassificationPipeline(model=new_model, tokenizer=tokenizer, return_all_scores=True)
PipelineInterface = TextClassificationPipeline(model=new_model, tokenizer=tokenizer, top_k=None, return_all_scores=True)


text="你的行為真讓我感到噁心"
result = PipelineInterface(text)
print()
print(text)
for res in result:
    for r in res:
        print(r)
    print("\n")