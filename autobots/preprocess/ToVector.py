from gensim import corpora
from collections import Counter

class ToVector:

    def __init__(self,list):
        '''

        :param list: init the ToVector class with the segmented sentences.txt list
                        so that ToVector can built dictionary with those sentences
        '''
        self.sentence_list=list
        self.words_bag = self.getskwordsbag()

    def togensimvector(self):
        '''
        分好词的句子列表作为语料 获取词典
        将文档转化成按gensim词频表示的向量
        '''
        dictionary = corpora.Dictionary(self.sentence_list)

        corpus = [dictionary.doc2bow(segment) for segment in self.sentence_list]

        return corpus

    def is_number(self,s):
        '''
        函数 is_number() 方法来判断字符串是否为数字
        '''
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def getskwordsbag(self):
        '''
        先执行getwordsbag（）获取词典，再利用此词典运行除分词外的其他函数（每次词语顺序不一样）
        :return: words bag built with the sentences.txt list in the initializer
        '''
        words_bag = set([])

        for doc in self.sentence_list:

            words_bag = words_bag | set(doc)

        no_num_bag=[word for word in list(words_bag) if not self.is_number(word)]# remove those numbers
        return no_num_bag



    def toskvector(self):
        '''
        #Count类 实验
        from  collections import Counter
        c=Counter(['空间','空间','空间','空间','空间','空间','这方面', '用料', '储物', '算是', '少', '\ufeff', ])
        print(c['空间'])
        #输出 6
        '''
        vec_list=[]


        for line in self.sentence_list:
            vec = []
            for w in self.words_bag:
                c = Counter(line)
                vec.append(c[w])
            vec_list.append(vec)
        return vec_list


    def toskvector_withlabel(self,tended_list,label):
        '''

        :param tended_list: list of segmented sentences.txt
        :param label: classify label for the sentences.txt represented by number
        :return: a list of vector representing those sentences.txt whitch ends with the label
        '''
        vec_list = []
        for line in tended_list:
            vec = []
            for w_index in range(len(self.words_bag)):
                c = Counter(line)
                # print(words_bag[w_index]+" "+str(c[words_bag[w_index]]))
                vec.append(c[self.words_bag[w_index]])
            vec.append(label)
            vec_list.append(vec)
        return vec_list
        # vec_list = []
        #
        #
        # for line in tended_list:
        #     vec = []
        #     for w in words_bag:
        #         c = Counter(line)
        #         vec.append(c[w])
        #         vec.append(label)
        #     vec_list.append(vec)
        # return vec_list