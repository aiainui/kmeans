kmeans聚类过程

1、训练词向量

'''
参考资料url：http://www.52nlp.cn/中英文维基百科语料上的word2vec实验
①准备数据，这里假设使用wiki百科的1G数据，其中需要做一个繁体转简体，转格式为utf8，分词过程，参见上面的博客，这里我已经转好了，下载地址见百度网盘：https://pan.baidu.com/s/1htn3gig passwd:d6ss。
②安装好python以及对应的模块 gensim，这里我们是用 gensim训练词向量
③写训练词向量的python脚本，参见上面的博客
④开始训练
'''

开始词向量的训练，如下命令，请在命令行下执行：
python train_word2vec_model.py wiki.zh.text.jian.utf-8.seg wiki.zh.text.model wiki.zh.text.vector >log.txt &

2、对已经准备好的聚类的语料（XHJ_wordsegment.txt）进行两步操作：清理，分词，这里我已经处理好了

'''清理的方法见（filterCharacter()），分词的方法见（）'''

3、计算每一行的文本的向量和

'''
①由于聚类需要计算每一行文本的向量，这里我们将所有分好的词的向量和作为该行文本的向量表示
②由于文本数据过多，所以我们将文本分按照10000条为单位进行了分割，分别求各个文件中文本的向量和，最终再做一次合并
'''

文本分割
DIV()
分别求每个文件中文本的向量和
calVec()
合并求出来的每个文件的向量和
sumvec()

4、kmeans聚类

save_cluster_results()

5、抽取聚类结果

saveRes()
