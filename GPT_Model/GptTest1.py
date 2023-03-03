import torch
import jieba
from transformers import GPT2Tokenizer, GPT2LMHeadModel
# 載入 GPT-2 模型
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

# 讀取文本
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 分詞
segments = jieba.cut(text)
text_segmented = "".join(segments)

# 進行文本摘要
input_text = "很好吃"
input_segmented = "".join(jieba.cut(input_text))
input_ids = tokenizer.encode(input_segmented, return_tensors="pt").to(device)
output = model.generate(
    input_ids.to(device),
    max_length=100,
    num_beams=1,
    early_stopping=True
)
summary = tokenizer.decode(output[0], skip_special_tokens=True)

print(summary)
