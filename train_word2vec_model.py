# 训练词向量的python脚本如下：
# 这里相关参数的调整，这里我们默认词向量维数为50，窗口为5，最少词数目为5，工作数为默认系统工作数；详情请参考https://radimrehurek.com/gensim/models/word2vec.html中的说明。
# train_word2vec_model.py

'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    # check and process input arguments
    if len(sys.argv) < 4:
        print (globals()['__doc__'] % locals())
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]
    model = Word2Vec(LineSentence(inp), size=40, window=5, min_count=5,
            workers=multiprocessing.cpu_count())
    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)
    model.save(outp1)
    model.save_word2vec_format(outp2, binary=False)
'''
