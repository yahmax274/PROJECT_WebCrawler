##使用CKIP分詞測試
from ckip_transformers import __version__
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker
from CKIPTransformers import ws_driver, pos_driver, ner_driver

# # Show version
# print(__version__)

# # Initialize drivers
# print("Initializing drivers ... WS")
# ws_driver = CkipWordSegmenter(model="albert-base", device=0)
# print("Initializing drivers ... POS")
# pos_driver = CkipPosTagger(model="albert-base", device=0)
# print("Initializing drivers ... NER")
# ner_driver = CkipNerChunker(model="albert-base", device=0)
# print("Initializing drivers ... all done")
# print()

def clean(sentence_ws, sentence_pos):
  short_with_pos = []
  short_sentence = []
  stop_pos = set(['Nep', 'Nh', 'Nb']) # 這 3 種詞性不保留
  for word_ws, word_pos in zip(sentence_ws, sentence_pos):
    # 只留名詞和動詞
    is_N_or_V = word_pos.startswith("V") or word_pos.startswith("N")
    # 去掉名詞裡的某些詞性
    is_not_stop_pos = word_pos not in stop_pos
    # 只剩一個字的詞也不留
    is_not_one_charactor = not (len(word_ws) == 1)
    # 組成串列
    if is_N_or_V and is_not_stop_pos and is_not_one_charactor:
      short_with_pos.append(f"{word_ws}({word_pos})")
      short_sentence.append(f"{word_ws}")
  return (" ".join(short_sentence), " ".join(short_with_pos))
def main():
    text = ["經過多年激烈戰事，複製人大戰即將結束。絶地議會派歐比王將導致戰亂的主謀者繩之以法；"
            "不料，西斯勢力已悄悄深入銀河系，勢力漸大的議長白卜庭用黑暗勢力的力量，誘惑天行者安納金轉變成黑武士達斯維達，"
            "幫助他達成心願建立銀河帝國，剷除絕地武士…【星際大戰】系列電影最後一塊拼圖，喬治盧卡斯不僅要解開黑武士的影壇跨世紀謎團，"
            "更要著手打造影史最大星際戰爭。"]
    ws = ws_driver(text)
    pos = pos_driver(ws)
    ner = ner_driver(text)
    print()
    print('=====')
    for sentence, sentence_ws, sentence_pos, sentence_ner in zip(text, ws, pos, ner):
        print("原文：")
        print(sentence)
        (short, res) = clean(sentence_ws, sentence_pos)
        print("斷詞後：")
        print(short)
        print("斷詞後+詞性標注：")
        print(res)
        print('=====')
if __name__ == "__main__":
    main()