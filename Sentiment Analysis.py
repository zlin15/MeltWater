
from snownlp import SnowNLP
from snownlp import classification
from snownlp import seg

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




