#encoding=utf-8
import jieba
import jieba.analyse


content = open('lyric.txt', 'rb').read()
cotent=0
#print ("Input：%s"%(content))

words = jieba.cut(content, cut_all=False)

#print "Output 精確模式 Full Mode："
for word in words:
	print ("%s"%(word))
	#print(type(word))
	if word == '關燈':
		print(456456456456464465465)




#從這個文章中取出前 10 個 tf-idf 值最大的關鍵詞。
"""
tags = jieba.analyse.extract_tags(content, 10)
print("Output：")
print(",".join(tags))
"""