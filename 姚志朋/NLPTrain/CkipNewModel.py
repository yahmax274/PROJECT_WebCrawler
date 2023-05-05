##呼叫Getdata
from Getdata import train_rows
##開始訓練
from sklearn import metrics
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import BertTokenizer, BertModel, BertConfig, BertTokenizerFast
import numpy as np
import pandas as pd


numpy_data = np.array(train_rows)
numpy_data = pd.DataFrame(data=numpy_data)
trainset, testset = train_test_split(numpy_data, test_size=0.2, random_state = 2022)
trainset, testset = trainset.reset_index(), testset.reset_index()

class CustomDataset(Dataset):

    def __init__(self, dataframe, tokenizer, max_len):
        self.tokenizer = tokenizer
        self.data = dataframe
        self.title = dataframe[1]
        self.targets = dataframe[0]
        self.max_len = max_len

    def __len__(self):
        return len(self.title)

    def __getitem__(self, index):
        title = str(self.title[index])
        title = " ".join(title.split())

        inputs = self.tokenizer.encode_plus(
            title,
            None,
            add_special_tokens=True,
            max_length=self.max_len,
            padding='max_length',
            return_token_type_ids=True,
            truncation=True
        )
        ids = inputs['input_ids']
        mask = inputs['attention_mask']
        token_type_ids = inputs["token_type_ids"]


        return {
            'input_ids': torch.tensor(ids, dtype=torch.long),
            'attention_mask': torch.tensor(mask, dtype=torch.long),
            'token_type_ids': torch.tensor(token_type_ids, dtype=torch.long),
            'labels': torch.tensor(self.targets[index], dtype=torch.float)
        }
    
    def samples(self):
      return [(title[:self.max_len], target) for target,title in zip(self.targets, self.title)]



#
max_seq_length = 75
tokenizer = BertTokenizerFast.from_pretrained('bert-base-chinese',max_length=max_seq_length,padding='max_length', truncation=True)
training_set = CustomDataset(trainset, tokenizer, max_seq_length)
validation_set = CustomDataset(testset, tokenizer, max_seq_length)

from transformers import DataCollatorWithPadding, AutoModelForSequenceClassification, TrainingArguments, Trainer
import torch

# Define model
def model_init():
  return AutoModelForSequenceClassification.from_pretrained(
      "ckiplab/bert-base-chinese", 
      num_labels=3,
      output_attentions = False, # Whether the model returns attentions weights.
      output_hidden_states = False,
      return_dict=True,
      id2label={0: '正面', 1: '中性', 2: '負面'   }
  )

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
training_args = TrainingArguments(
    output_dir="./NewResults100",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=15,
    weight_decay=0.01,
    logging_steps=10,
    save_steps=5,
    seed=2022,
    data_seed=2022,
    evaluation_strategy="steps",
    eval_steps=5

)

trainer = Trainer(
    model_init=model_init,
    args=training_args,
    train_dataset=training_set,
    eval_dataset=validation_set,
    tokenizer=tokenizer,
    data_collator=data_collator

)

trainer.train()