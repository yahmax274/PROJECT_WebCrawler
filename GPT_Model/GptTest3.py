##讀取整篇文章，進行摘要
# 用於大文本
import torch
import jieba
from transformers import pipeline, set_seed, GPT2Tokenizer, GPT2LMHeadModel

# 設置隨機種子
set_seed(42)

# 初始化 tokenizer 和 model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
model = GPT2LMHeadModel.from_pretrained('gpt2-medium', pad_token_id=tokenizer.eos_token_id, return_dict=True)

# 修改模型最大長度
model.config.max_position_embeddings = 2048

# 輸入句子
input_text = "旅行的意義？"

# 將句子轉換為 token
input_ids = tokenizer.encode(input_text, return_tensors='pt')

if input_ids is not None:
    # 限制輸入序列的長度
    max_length = 1024
    if input_ids.shape[-1] > max_length:
        input_ids = input_ids[:, :max_length]

    # 生成文字
    output = model.generate(
                input_ids=input_ids,
                max_length=max_length + 20, # 增加輸出序列的長度
                do_sample=True,
                temperature=0.7,
                num_return_sequences=1,
                pad_token_id=tokenizer.eos_token_id, # 設置 pad token
                attention_mask=input_ids.ne(tokenizer.pad_token_id).float() # 設置 attention mask
            )

    # 解碼生成的 token
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # 輸出結果
    print(output_text)
else:
    print("Failed to generate input_ids.")

