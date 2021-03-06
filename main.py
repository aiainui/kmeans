# **********************************代码区****************************#

# 简繁体转换代码
from langconv import *


def simple2tradition(line):
    # 将简体转换成繁体
    line = Converter('zh-hant').convert(line.decode('utf-8'))
    line = line.encode('utf-8')
    return line


def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line.decode('utf-8'))
    line = line.encode('utf-8')
    return line





# 清理数据代码
# 这里我们留下中文和数字即可
def filterCharacter(s):
    import re
    # s = u"中文bab#$%[][]【】273080吗jlasud90^*^&)!@708)*_@$#%#$"
    # r = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", s)

    print('filter start is :', s)
    r1 = re.sub(u"[^\u4e00-\u9fa5|0-9]", " ", s)
    r1 = re.sub(r"\s{1,}", "", r1)
    print('filter result is :', r1)
    return r1


# 分词代码，这里使用jieba分词
def wordsegment(sentence):
    import jieba
    # 清理非法的字符
    # question = filterCharacter(sentence)
    print('...cut sentence..')
    seg_list = jieba.cut(sentence, cut_all=False, HMM=True)
    # print('分词结果为:',' '.join(seg_list))
    return ' '.join(seg_list)


# 将40W小黄鸡的数据以10000条为单位存入/data目录下：
# -*- coding: utf-8 -*-
def DIV():
    destpathQ_jieba_ok = r'./XHJ_wordsegment.txt'
    count = 0
    with open(destpathQ_jieba_ok, 'r', encoding='utf-8') as destpathQ_jieba_ok:
        for line in destpathQ_jieba_ok:
            count += 1
            data = count / 10000
            with open('./data/' + str(int(data)) + '.txt', 'a') as infile:
                infile.write(line)
        print(count)


# 求/data下的所有文件的文本向量和，存入/vec下：
def calVec():
    import numpy as np
    import gensim
    model = gensim.models.Word2Vec.load("./wiki.zh.text.model")

    import os

    path = "./data"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    s = []
    for file in files:  # 遍历文件夹

        # print(file)

        file_des = file

        # destpathQ_jieba_ok = r'D:/python34/program/word_segment/XHJ_wordsegment.txt'
        destpathQ_jieba_ok = './data/' + file;
        print(destpathQ_jieba_ok)
        # destpathQ_WV = r'D:/python34/program/zhichi_QA/qa_utf8/qa_train_qc/all/zhichi_Q_WordVec.csv'
        sum = 0
        Qcount = 0
        dimension = 40

        sentencesVec = np.zeros((1, dimension))
        zeroVec = np.zeros(dimension)
        # print('sentencesVec',sentencesVec+sentencesVec)

        with open(destpathQ_jieba_ok, 'r', encoding='utf8') as infile:
            i = 0
            for file in infile:
                Qcount += 1
                print('Qcount---------------------------------------------------------:', Qcount)
                filelist = file.split(' ')
                for term in filelist:
                    print('terms ;', term)
                    vec1 = model[term]
                    # print('vec1:',vec1)
                    sum += vec1
                # print('sum',sum)

                if ((zeroVec == sum).all()):
                    sum = np.zeros((dimension))
                sentencesVec = np.concatenate((sentencesVec, [sum]), axis=0)
                if (Qcount == 1):
                    sentencesVec = sentencesVec[1:, ]
                    print('setencesVec', sentencesVec)
                # print('sentencesVec',sentencesVec)
                print('size of sentencesVec is : ', sentencesVec.shape)
                # if ((zeroVec == sum).all()):
                #     break;
                sum = 0
            np.savetxt('./vec/' + file_des[:-4] + '.Vec', (sentencesVec))


# 合并求出的各个向量和文件
# -*- coding: utf-8 -*-
def sumvec():
    import numpy as np

    demension = 40
    data = np.zeros((1, demension))

    for i in range(41):
        print('file------>:', i)
        path = r'./vec/' + str(int(i)) + '.Vec'
        data1 = np.loadtxt(path)

        data = np.concatenate((data, data1), axis=0)

    print(data.shape)

    np.savetxt('./sum.Vec', (data))


# kmeans聚类
def save_cluster_results():
    import numpy as np
    from sklearn.cluster import KMeans
    data = np.loadtxt('./sum1.Vec')
    # print(data)
    # 假如我要构造一个聚类数为3的聚类器
    estimator = KMeans(n_clusters=100, n_jobs=3)  # 构造聚类器
    estimator.fit(data)  # 聚类
    label_pred = estimator.labels_  # 获取聚类标签
    print("label_pred", label_pred)
    np.savetxt('label_pred', (label_pred))
    centroids = estimator.cluster_centers_  # 获取聚类中心
    np.savetxt('centroids', (centroids))
    print('centriods', centroids)
    inertia = estimator.inertia_  # 获取聚类准则的总和
    print("inertia", inertia)


# 将分好类的文件存起来：
def saveRes():
    import numpy as np
    label_pred = np.loadtxt('./label_pred')

    filepath = r'./res/km'
    scanpath = r'./XHJ_qc.txt'
    i = 0
    with open(scanpath, 'r', encoding='utf8') as scanfile:
        for question in scanfile:
            print(label_pred[i])
            with open(filepath + str(int(label_pred[i])) + '.txt', 'a', encoding='utf8') as infile:
                infile.write(question)
            i += 1
© 2018 GitHub, Inc.
