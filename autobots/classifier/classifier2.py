from Autobots.preprocess.FileToSeg import ToSegSenList
from Autobots.preprocess.ToVector import ToVector

ts=ToSegSenList("./stop_words.txt")

pos_list=ts.get_file_seg(path="./内饰正.txt")
neg_list=ts.get_file_seg(path="./内饰负.txt")

print(pos_list)
tv=ToVector(pos_list+neg_list)
words_bag=tv.getskwordsbag()
print("words bag length: "+str(len(words_bag)))#1538 words in total

posset= tv.toskvector_withlabel(pos_list[:135],1)
negset=tv.toskvector_withlabel(neg_list[:135],0)

dataset=posset+negset
print(len(dataset))
# for vec in dataset[130:140]:
#     print(vec)

import numpy as np
from sklearn import cross_validation

npdataset=np.array(dataset)
print("numpy data set:")
print(npdataset)
train_data=npdataset[:,:-1]
train_target=npdataset[:,-1]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_data, train_target, test_size=0.4, random_state=0)


from sklearn.naive_bayes import GaussianNB
models=GaussianNB()
models.fit(X_train,y_train)

predict=models.predict(X_test)
hit=0.0
total=len(predict)
for p in range(len(predict)):

    if predict[p]==y_test[p]:
        hit+=1
print("hit rate: "+str(hit/total))

from sklearn.ensemble import RandomForestClassifier
clf= RandomForestClassifier(100)
clf.fit(X_train,y_train)
predict=clf.predict(X_test)
hit=0.0
total=len(predict)
for p in range(len(predict)):

    if predict[p]==y_test[p]:
        hit+=1
print("hit rate: "+str(hit/total))


sentence=[" 做工精细，对于10多年前的车，顶棚有脱落的迹象。",
"  不落伍",
" 很好，使用方便",
" 用料还是讲究的，做工是严谨的",
" 经典  沉稳大气  大方"]
sen_list=ts.get_seg(sentence)
sen_vec=tv.toskvector_withlabel(sen_list,1)
np_sen_vec=np.array(sen_vec)
predicted=models.predict(np_sen_vec[:,:-1])
for p in predicted:
    print(p)






