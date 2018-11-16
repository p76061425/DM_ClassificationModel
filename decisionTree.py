import numpy as np
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import graphviz
import re
import pydotplus
import argparse

def read_dataBase(path):
    with open( path, 'rt') as f:
        database = f.read()
    data = re.split(r'[\n]',database)
    attributes_list = data[0].split()
    attributes_list.remove("class")
    del data[0] 
    
    tdb = []
    label = []
    for line in data:
        item = line.split()
        item = list(map(int, item))
        if( len(item)!=0 ):
            label.append(item[5])
            del item[5]
            tdb.append(item)    
        
    return np.array(tdb),np.array(label),attributes_list
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-train',
                        default="./data/train_data.txt",
                        dest='TRAIN_PATH',
                        help='Input training data file, default = ./data/train_data.txt ')
    parser.add_argument('-test',
                        default="./data/test_data.txt",
                        dest='TEST_PATH',
                        help='Input testing data file, default = ./data/test_data.txt ')
    args = parser.parse_args()
    
    train_data_path = args.TRAIN_PATH
    test_data_path = args.TEST_PATH
    x_train,y_train,attributes_list = read_dataBase(train_data_path)
    
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    
    x_test,y_test,attributes_list = read_dataBase(test_data_path)
    pridict_label = clf.predict(x_test)

    
    aaaaa = [3, False, 2, -34606, 0 ]
    pridict_label = clf.predict(x_test)

    
    T0 = 0
    T1 = 0
    T2 = 0
    F0 = 0
    F1 = 0
    F2 = 0
    for pridict,y in zip(pridict_label,y_test):
        if(pridict == y):
            if(pridict == 0):
                T0 += 1
            elif(pridict == 1):
                T1 += 1
            else:
                #print(pridict,y)
                T2 += 1
        else:
            if(pridict == 0):
                F0 += 1
            elif(pridict == 1):
                F1 += 1
            else:
                F2 += 1
              
    accuracy = (T0+T1+T2) / (T0+T1+T2+F0+F1+F2)
    precision_0 = T0 / (T0+F0)
    precision_1 = T1 / (T1+F1)
    precision_2 = T2 / (T2+F2)
    recall_0 = T0 / (T0+F1+F2)
    recall_1 = T1 / (T1+F0+F2)
    recall_2 = T2 / (T2+F0+F1)
    
    print("accuracy",accuracy)
    print("precision_0",precision_0)
    print("precision_1",precision_1)
    print("precision_2",precision_2)
    print("recall_0",recall_0)
    print("recall_1",recall_1)
    print("recall_2",recall_2)

    dot_data = export_graphviz(clf, out_file=None, feature_names=attributes_list, filled=True,rounded=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("tree.pdf")

