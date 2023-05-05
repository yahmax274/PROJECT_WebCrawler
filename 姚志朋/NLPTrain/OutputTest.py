##模型驗證
from transformers import TextClassificationPipeline
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from transformers import AutoTokenizer

# Model_Location="./results/checkpoint-15/"
# Model_Location="./NTUSD_results/checkpoint-115/"NewResults
# Model_Location="./NewResults/checkpoint-15/"
Model_Location="./NewResults100/checkpoint-150/"
new_model = AutoModelForSequenceClassification.from_pretrained(Model_Location,output_attentions=True)
tokenizer = AutoTokenizer.from_pretrained(Model_Location)
# PipelineInterface = TextClassificationPipeline(model=new_model, tokenizer=tokenizer, return_all_scores=True)
PipelineInterface = TextClassificationPipeline(model=new_model, tokenizer=tokenizer, top_k=None, return_all_scores=True)

# text="廁所跟浴室獨立，但廁所沒有免治，小扣分。"
# text="靠近大眾運輸站 · 附近有購物區和觀光景點 · 適合開車前往"
text="你的行為真讓我感到噁心"
# text="自己也有去慈惠堂現場看排隊，他坦言隊伍「真的很長」"
result = PipelineInterface(text)
print()
print(text)
for res in result:
    for r in res:
        print(r)
    print("\n")


