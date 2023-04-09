##模型驗證
from transformers import TextClassificationPipeline
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
new_model = AutoModelForSequenceClassification.from_pretrained("./results/checkpoint-15/",output_attentions=True)

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("./results/checkpoint-15/")

PipelineInterface = TextClassificationPipeline(model=new_model, tokenizer=tokenizer, top_k=None, return_all_scores=True)
# text="廁所跟浴室獨立，但廁所沒有免治，小扣分。"
text="靠近大眾運輸站 · 附近有購物區和觀光景點 · 適合開車前往"
result = PipelineInterface(text)
print()
print(text)
for res in result:
    for r in res:
        print(r)
    print("\n")
