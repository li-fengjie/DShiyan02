import jieba
import numpy as np
import wordcloud
# a=jieba.lcut("我中华民国")
# print(a)
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
txt = open("all.txt","r",encoding='utf-8').read()
extxt=open("stopword.txt","r",encoding='utf-8').read()
# name_list = ['宝玉', '黛玉', '宝钗', '元春', '探春', '湘云', '妙玉', '迎春', '惜春', '凤姐', '熙凤', '巧姐', '李纨', '可卿', '贾母', '贾珍', '贾蓉', '贾赦', '贾政', '王夫人', '贾琏', '薛蟠', '香菱', '宝琴', '袭人', '晴雯', '平儿', '紫鹃', '莺儿']

exwords=jieba.lcut(extxt)
excounts={}
for exword in exwords:
    if len(exword)==1:
        continue
    else:
        excounts[exword] = excounts.get(exword, 0) + 1
excludes=set(excounts)


words=jieba.lcut(txt)

counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
# excludes={"什么","一个","我们","那里","你们","如今","说道","知道","老太太","起来","姑娘","这里","出来","他们","众人","自己"
#           ,"一面","太太","只见","怎么","奶奶","两个","没有","不是","不知","这个","听见","这样","进来","咱们","告诉","就是"
#           ,"东西","平儿","回来","只是","大家","老爷","只得","丫头","这些","不敢","出去","凤姐儿","所以","不过","的话","不好"
#           ,"姐姐"}
for word in excludes:
        del(counts[word])

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
s=[]
for i in range (10):
    word,count=items[i]
    s.append("{0:<10}".format(word))
str=" ".join(s)

print(str)
font_path="C:\Windows\Fonts\STXINWEI.TTF"
img=Image.open("li.jpg")
bg_pic = np.array(img)

wd = WordCloud(mask=bg_pic,background_color='white',font_path=font_path,width=200,height=135,margin=1,max_words=2000
               ,relative_scaling=0.4,min_font_size=5).generate(str)
wd.to_file('0.png')