import jieba



class ToSegSenList:

    def __init__(self,stopwordpath):
        self.stopwordpath=stopwordpath
        self.stopwords=self.read_file(self.stopwordpath).split("\n")

    def read_file(self,path):

        with open(path) as f:
            return f.read()

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



    def get_file_seg(self,path):
        '''
        将各文档分词，从字符串转化为单词列表
        '''
        sen_list=self.read_file(path=path).split("\n")
        stopwords=self.stopwords
        return self.get_seg(sen_list=sen_list)

    def get_seg(self, sen_list):
        stopwords = self.stopwords
        seg_list = [[word for word in jieba.cut(document) if word not in stopwords and not self.is_number(word)]
                    for document in sen_list]

        return seg_list

    def get_sentence_seg(self,sentence):
        '''
        从字符串转化为单词列表
        '''
        stopwords = self.stopwords
        return [[word for word in jieba.cut(sentence) if word not in stopwords and not self.is_number(word)]]



# ts=ToSegSenList()
# print(ts.get_seg_list(path="/home/konroy/PycharmProjects/Autobots/modules/内饰正.txt"))