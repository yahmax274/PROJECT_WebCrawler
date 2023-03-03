from transformers import MT5ForConditionalGeneration, MT5Tokenizer

# model_name = 'google/mt5-small'
# model_name = 'google/mt5-base'
model_name = 'google/mt5-large'

model = MT5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = MT5Tokenizer.from_pretrained(model_name)

# 定義輸入文本
input_text = '人生的道路充滿了艱辛和挑戰，但也有美好的瞬間和機會。'

# 將輸入文本編碼成模型可接受的形式
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# 使用模型生成下一個文本
# outputs = model.generate(input_ids)
# outputs = model.generate(input_ids, max_new_tokens=50)
outputs = model.generate(input_ids, max_length=50, min_length=5)

# 將生成的文本解碼成人類可讀的形式
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
'''
# 讀取CSV檔案
df = pd.read_csv("your_file.csv")

# 循環處理每一行文本
for index, row in df.iterrows():
    input_text = row["your_text_column_name"]
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Input Text:", input_text)
    print("Generated Text:", generated_text)
'''
