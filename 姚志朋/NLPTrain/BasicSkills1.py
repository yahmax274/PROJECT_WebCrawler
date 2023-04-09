# import jieba
# text="很美的地方，天氣很涼爽，不過停車場比較小假日來有可能沒地方停車啊🥹隧道有告示牌請勿進入，還是有看到遊客進入，感覺土石鬆軟有些危險，所有不要當新聞頭條哦！有咖啡店還有伴手禮商店，冰一支40元便宜好吃又濃郁，拿鐵一杯110個人覺得和價格比較沒那麼ok。 …"
# # seg_list = jieba.cut("我是胖虎我是孩子王", cut_all=True)
# seg_list = jieba.cut(text, cut_all=True)
# print("Paddle Mode: " + "/ ".join(seg_list))  # paddle模式

import unittest

import ckip


class CKIPUnittest(unittest.TestCase):
    # def test_Segment(self):
    #     c = ckip.CKIP('iis', 'iis')
    #     res = c.Segment('台新金控12月3日將召開股東臨時會進行董監改選。'
    #                     '這是一個中文句子。')
    #     self.assertEquals(len(res), 2)

    def test_Invalid_Credential(self):
        c = ckip.CKIP('abc', '123')
        with self.assertRaisesRegexp(RuntimeError, 'Authentication failed'):
            res = c.Segment('台新金控12月3日將召開股東臨時會進行董監改選。'
                            '這是一個中文句子。')


if __name__ == '__main__':
    unittest.main()