from transformers import MT5Tokenizer, MT5ForConditionalGeneration

tokenizer = MT5Tokenizer.from_pretrained('google/mt5-small')
model = MT5ForConditionalGeneration.from_pretrained('google/mt5-small')
##訓練參數
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=1,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    prediction_loss_only=True,
)
#定義訓練數據集
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, data):
        self.data = data
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return {'input_ids': self.data[idx]['input_ids'],
                'attention_mask': self.data[idx]['attention_mask'],
                'decoder_input_ids': self.data[idx]['target_ids'][:-1],
                'decoder_attention_mask': self.data[idx]['target_mask'][:-1],
                'labels': self.data[idx]['target_ids'][1:]}
#加載訓練數據
import json
from torch.utils.data import DataLoader
import torch

with open('train_data.json') as f:
    train_data = json.load(f)

train_dataset = MyDataset(train_data)
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
#訓練模型
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=lambda data: {'input_ids': torch.stack([item['input_ids'] for item in data]),
                               'attention_mask': torch.stack([item['attention_mask'] for item in data]),
                               'decoder_input_ids': torch.stack([item['decoder_input_ids'] for item in data]),
                               'decoder_attention_mask': torch.stack([item['decoder_attention_mask'] for item in data]),
                               'labels': torch.stack([item['labels'] for item in data])}
)

trainer.train()

'''
import pandas as pd
from transformers import MT5Tokenizer

tokenizer = MT5Tokenizer.from_pretrained('google/mt5-small')

# 讀取CSV檔案
data = pd.read_csv('data.csv')

# 轉換為訓練模型需要的格式
inputs = tokenizer(data['text'].tolist(), padding=True, truncation=True, return_tensors='pt')
labels = tokenizer(data['label'].tolist(), padding=True, truncation=True, return_tensors='pt')

# 訓練模型（假設使用transformers套件內建的Trainer類別）
from transformers import MT5ForConditionalGeneration, Trainer, TrainingArguments

model = MT5ForConditionalGeneration.from_pretrained('google/mt5-small')
training_args = TrainingArguments(
    output_dir='./results',          # 訓練結果的儲存路徑
    num_train_epochs=1,              # 訓練回合數
    per_device_train_batch_size=16,  # 批次大小
    warmup_steps=500,                # 學習率線性增加的步數
    learning_rate=5e-5,              # 初始學習率
    logging_dir='./logs',            # 訓練日誌儲存路徑
    logging_steps=10,                # 多少步驟輸出一次日誌
    evaluation_strategy='steps',     # 在何時進行評估（steps表示每N步驟進行一次）
    eval_steps=50,                   # 多少步驟進行一次評估
    save_total_limit=1,              # 最多儲存幾個checkpoint
    save_steps=100,                  # 多少步驟儲存一個checkpoint
)

trainer = Trainer(
    model=model,                         # 要訓練的模型
    args=training_args,                  # 訓練相關的參數
    train_dataset=inputs,                # 訓練集
    data_collator=lambda data: {'input_ids': data['input_ids'], 'attention_mask': data['attention_mask'], 'labels': data['input_ids']},  # 將inputs轉換為模型輸入格式
)

trainer.train()
#以上範例程式碼假設你的CSV檔案包含text和label兩個欄位，其中text欄位包含訓練資料的文本內容，label欄位包含訓練資料的標籤內容。
'''