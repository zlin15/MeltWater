
from snownlp import SnowNLP
from snownlp import classification
from snownlp import seg
import glob
txt=glob.glob('*.txt')
for k in range(29,49):
    a = str(k)+'.txt'
    txt = open(a)
    read_txt=txt.read()
    s = SnowNLP(read_txt)
    print('sentiment for article %s is: ' %k + str(s.sentiments))
    # keywords = s.keywords(200)
    # summary = s.summary(30)
    # s_sentences=s.sentences
    # for i in s_sentences:
    #     print(i,)
    #     sen = SnowNLP(i)
    #     print(sen.sentiments)
# print(s.sentiments)
#
#


# from snownlp import normal
# from snownlp import seg
# from snownlp.summary import textrank
#
#
# if __name__ == '__main__':
#     txt = open('10.txt')
#     read_txt = txt.read()
#     t = normal.zh2hans(read_txt)
#     sents = normal.get_sentences(t)
#
#     doc = []
#     for sent in sents:
#         words = seg.seg(sent)
#         words = normal.filter_stop(words)
#         doc.append(words)
#     rank = textrank.TextRank(doc)
#     rank.solve()
#     for index in rank.top_index(5):
#         print(sents[index])
#     keyword_rank = textrank.KeywordTextRank(doc)
#     keyword_rank.solve()
#     for w in keyword_rank.top_index(5):
#         print(w)
#



