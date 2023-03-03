from transformers import MT5ForConditionalGeneration, MT5Tokenizer
import torch

# 加载已经微调好的MT5-base模型和分词器
model = MT5ForConditionalGeneration.from_pretrained('path/to/fine-tuned/model')
tokenizer = MT5Tokenizer.from_pretrained('google/mt5-small')

# 输入要进行情感分析的文本
text = "这是一段测试文本，我们将使用MT5模型对其进行情感分析。"

# 将文本进行分词和编码
input_ids = tokenizer.encode(text, return_tensors='pt')

# 将输入传递到模型中进行推理
outputs = model.generate(input_ids=input_ids, max_length=2)

# 解码输出，获取情感标签
sentiment = tokenizer.decode(outputs[0])
if sentiment == '0':
    print('Negative')
elif sentiment == '1':
    print('Positive')
else:
    print('Neutral')