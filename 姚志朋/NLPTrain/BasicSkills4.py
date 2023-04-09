##利用CKIP Transformers進行情感分析
train_rows = [
 [[1, 0, 0],
  "乾淨不受打擾。沒有櫃台人員是十分信認顧客的地方，雖然或許少了點噓寒問暖的親切，卻也多了一份不受監視的自在感。"],
 [[1, 0, 0],
  "民宿老闆跟老闆娘親切。茶水間附設許多電器及泡麵，很多民宿沒有這樣的服務"],
 [[1, 0, 0],
  "環境舒適，房間很安靜，兒童遊樂物品多，老闆夫妻很親切人很好，很優質。"],
 [[1, 0, 0],
  "溜滑梯房設計很好孩子很喜歡民宿老闆老闆娘很友善👍"],
 [[1, 0, 0],
  "老闆、老闆娘都很親切，還推薦很多可以去玩的地方，真的很不錯唷！"],
 [[1, 0, 0],
  "適合親子住宿且小朋友住到捨不得離開,商圈熱閙採買方便,下次還會來住!"],
 [[1, 0, 0],
  "兒童遊戲區及嬰兒配套"],
 [[1, 0, 0],
  "育兒用品幾乎全部都有非常方便，環境舒適整潔，地點方便。房間內有溜滑梯可玩，而且容易撞到的地方都有貼防撞條非常細心，也有整齊乾淨的公共遊戲室。要停車可事先預約。如果有帶小孩來花蓮玩非常推薦住這裡。"],
 [[1, 0, 0],
  "房間的溜滑梯讓小孩開心極了，其他的兒童遊戲間及電動車也都很受歡迎，為兒童準備的沐浴用品選用Fees也相當用心，整體都布置得相當別緻而且乾淨"],
 [[1, 0, 0],
  "床很舒服環境很乾淨主人家很親切小小孩很開心交通方便機能很好很棒的住宿經驗"],
 [[0, 0, 1],
  "如果價格可以在便宜一點點會更好."],
 [[0, 0, 1],
  "電視位置不好，不能正面看到電視"],
 [[0, 0, 1],
  "床邊的牆用防撞牆紙會更好，因為B B撞了很多次"],
 [[0, 0, 1],
  "溜滑梯上鋪的地毯有些不適合容易受傷，床鋪上方的溜滑梯大人容易撞到頭或許可以加個邊角保護墊?"],
 [[0, 0, 1],
  "沒有。"],
 [[0, 0, 1],
  "隔音稍差"],
 [[0, 0, 1],
  "沒有"],
 [[0, 0, 1],
  "牆壁上沒有掛鉤可以掛衣服"],
 [[0, 0, 1],
  "沒有衣櫃，衣服多，無法掛"],
 [[0, 0, 1],
  "早餐沒有選擇性,口味一般,有點可惜"],
]

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
    output_dir="./results",
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