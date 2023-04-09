##使用 SnowNLP 進行情感分析
# from snownlp import SnowNLP
# text = "我今天很快樂。我今天很憤怒。" 
# s = SnowNLP(text)
# s.sentences
# s.words
# #SnowNLP的情感分析取值，表達的是“這句話代表正面情感的概率”。
# print(SnowNLP(s.sentences[0]).sentiments)
# print(SnowNLP(s.sentences[1]).sentiments)
# print(s.sentiments)
from transformers import DataCollatorWithPadding, AutoModelForSequenceClassification, TrainingArguments, Trainer