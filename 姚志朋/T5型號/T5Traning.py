from transformers import T5Tokenizer, T5ForConditionalGeneration
from torch.utils.data import Dataset,DataLoader
from tqdm.auto import tqdm
import torch.utils.data as data
import pandas as pd
import torch
import transformers
############測試############
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# model_name = "google/mt5-small"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# input_text = "這是一個輸入文本。"
# input_ids = tokenizer.encode(input_text, return_tensors="pt")
# outputs = model.generate(input_ids=input_ids, max_length=128, num_beams=4, early_stopping=True)
# output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print("生成的文本：", output_text)
############測試############
class NewsSummary(Dataset):
    def __init__(self, text, summary, tokenizer,max_len = 512):
        self.data = []
        input_t = tokenizer(text,padding="longest")
        label_t = tokenizer(summary,padding="longest")

        for i,j,k in zip(input_t['input_ids'], input_t['attention_mask'], label_t['input_ids']):
            for cnt,tmp in enumerate(k):
                if tmp == 0:
                    k[cnt] = -100
                    
            self.data.append({'input_ids':torch.tensor(i[:max_len]),
                              'attention_mask':torch.tensor(j[:max_len]),
                              'labels':torch.tensor(k[:max_len])})

    def __getitem__(self, index):
        
         
        return self.data[index]
        

    def __len__(self):
        return len(self.data)
    
    
data = pd.read_csv("cl_news_summary.csv")
input_text = data['text'].tolist()[:200]
input_text = ["summarize: " + i for i in input_text]
summary = data['summary'].tolist()[:200]

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

train_set = NewsSummary(input_text, summary, tokenizer,max_len = 512)
train_loader = DataLoader(train_set,batch_size = 1,shuffle = True)

model.cuda()
optimizer = torch.optim.AdamW(params = model.parameters(), lr = 1e-4)
for epoch in range(30):
    model.train()
    train = tqdm(train_loader)
    for data in train:
        for key in data.keys():
            data[key] = data[key].cuda()
        outputs = model(**data)
        loss = outputs.loss
        train.set_description(f'Epoch {epoch}')
        train.set_postfix({'Loss': loss.item()})
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    
    model.save_pretrained('model_{}'.format(epoch))
print("----結束----")