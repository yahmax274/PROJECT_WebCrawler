##使用CPU運算
import torch
import transformers
import time
start = time.time()
model_name = 'google/mt5-small'
# model_name = 'google/mt5-base'
# model_name = 'google/mt5-large'

model = transformers.MT5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = transformers.T5Tokenizer.from_pretrained(model_name, pad_token='<pad>')

punctuations = { "，": ",", "。": ".", "！": "!", "？": "?", "；": ";", "：": ":", "「": "\"", "」": "\"", "（": "(", "）": ")" }

def custom_tokenizer(text, tokenizer):
    for key, value in punctuations.items():
        text = text.replace(key, value)
    return tokenizer(text, return_tensors='pt')

def generate_summary(input_text, max_length=256, min_length=10, num_beams=4):
    if not input_text:
        return "Error: Input text is empty."
    
    # 限制文本長度為前100個字元
    input_text = input_text[:100]
    
    input_ids = custom_tokenizer(input_text, tokenizer=tokenizer)

    summary_ids = model.generate(input_ids=input_ids['input_ids'],
                                    attention_mask=input_ids['attention_mask'],
                                    num_beams=num_beams,
                                    max_length=max_length,
                                    min_length=min_length,
                                    early_stopping=True,
                                    pad_token_id=tokenizer.pad_token_id)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)      
    return summary    

# input_text = "蘋果很好吃，爸爸覺得蘋果很好吃，媽媽覺得蘋果很好吃，我覺得蘋果很好吃，弟弟覺得蘋果很好吃。"
# input_text = "在這篇文章中，我們將探討MT5-large模型的基本原理以及如何用它來生成文章摘要。這是一篇範例文章，用於展示如何使用MT5-large模型來生成文章摘要。"
input_text ="由於管理者調整世界扭曲的行動失敗，長瀨香失去了肉體，而且無法再回到原本的世界，只能轉生至文明更為落後的世界。無法忍受自己被扔到那種地方的香提出要求，想要一種「可以自由做出任何效果藥品」的能力，並更進一步取得道具箱、語言理解能力及稍微返老還童的身體。就這樣，15 歲的少女‧香使用自己創造的藥品──魔法藥水，以穩定的生活為目標展開冒險。"
summary = generate_summary(input_text)
print(f'Summary: {summary}')
print("結束")
end = time.time()
print(end-start)





