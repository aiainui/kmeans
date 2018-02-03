def isStopWords(term):
    import pickle
    from tools import File_Interface as FI

    #seg_list = jieba.cut(question, cut_all=False, HMM=True)
    #senetence = r'吗'
    ret = []
    ret = FI.load_pickle('D:/python34/program/tools/stop_words.pkl')
    #print(ret)
    if(term in ret):
        return True
    else:
        return False


# result = isStopWords()
# print(result)