import numpy as np
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import graphviz
import re
import pydotplus
import argparse
from sklearn import metrics
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.pipeline import make_pipeline
import os
import sys
import pickle

def warn(*args, **kwargs):    
    pass

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
    parser.add_argument('-m',
                        default="dct",
                        dest='METHOD',
                        help='Classification method, dct=(Decision Tree),svm=(Support Vector Machine), default = dct ')    
    parser.add_argument('-train',
                        default="./data/train_data.txt",
                        dest='TRAIN_PATH',
                        help='Input training data file, default = ./data/train_data.txt ')
    parser.add_argument('-test',
                        default="./data/test_data.txt",
                        dest='TEST_PATH',
                        help='Input testing data file, default = ./data/test_data.txt ')
    parser.add_argument('-k',
                        default='rbf',
                        dest='KERNEL',
                        help='SVM kernel,default=rbf')    
    parser.add_argument('-c',
                        default='1',
                        dest='PENALTY_C',
                        help='SVM penalty parameter C of the error term,default=1')        
    parser.add_argument('-cv',
                        default='10',
                        dest='CV',
                        help='SVM cross_validate,default=10')                        
    args = parser.parse_args()
    
    train_data_path = args.TRAIN_PATH
    test_data_path = args.TEST_PATH
    x_train,y_train,attributes_list = read_dataBase(train_data_path)
    x_test,y_test,attributes_list = read_dataBase(test_data_path)
    
    train_size = x_train.shape
    test_size = x_test.shape
    print("train_size:",train_size)
    print("test_size:",test_size)
    
    method = args.METHOD
    
    if(method == "dct"):
        print("Method:",method,"(Decision Tree)\n")
        clf = DecisionTreeClassifier()
        clf.fit(x_train, y_train)
        
        y_pridict = clf.predict(x_test)

        dot_data = export_graphviz(clf, out_file=None, feature_names=attributes_list, filled=True,rounded=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf("tree.pdf")
        
        accuracy = metrics.accuracy_score(y_test, y_pridict)
        precision = metrics.precision_score(y_test, y_pridict, average='macro')
        recall = metrics.recall_score(y_test, y_pridict, average='macro')
        print("Result:")
        print("  Accuracy:",accuracy)
        print("  Precision:",precision)
        print("  Recall:",recall)
        

    elif(method == "svm"):
        print("Method:",method,"(Support Vector Machine)\n")
    
        import warnings
        warnings.warn = warn

        KERNEL = args.KERNEL
        PENALTY_C = float(args.PENALTY_C)
        CV = int(args.CV)

        print("SVM Kernel:",KERNEL)
        print("Penalty C:",PENALTY_C)
        print("Cross Validate:",CV,'\n')
        
        standard_scaler = StandardScaler()
        standard_scaler_result = standard_scaler.fit_transform(x_train)
        
        print("training...\r",end = "")
        svm_model = svm.SVC(gamma='scale', kernel=KERNEL, C = PENALTY_C, max_iter = 10000)
        svm_model.fit(standard_scaler_result, y_train)
        
        print("cross validate...\r",end = "")
        scores = cross_validate(svm_model, standard_scaler_result, y_train, cv=CV,
                            scoring=('precision_macro', 'recall_macro', 'accuracy'))

        cv_num = 0
        avg_train_acc = 0
        avg_train_pre = 0
        avg_train_rec = 0
        avg_test_acc  = 0
        avg_test_pre  = 0
        avg_test_rec  = 0
        print("Cross Validation Result:")
        print('|CV No.| Accuracy  | Percision | Recall   | Accuracy  | Percision | Recall    |')
        print('|---   |---        |---        |---       |---        |---        |---        |')
        print('|Type  | Train     | Train     | Train    | Test      | Test      | Test      |')
        for train_accuracy, train_precision, train_recall, \
            test_accuracy,  test_precision,  test_recall in \
            zip(scores['train_accuracy'], scores['train_precision_macro'], scores['train_recall_macro'], \
                scores['test_accuracy'],  scores['test_precision_macro'],  scores['test_recall_macro']):
            print('| cv{}  |  {:0.4f}   |  {:0.4f}   |  {:0.4f}  |  {:0.4f}   |  {:0.4f}   |  {:0.4f}   |'.format(cv_num, \
                  train_accuracy, train_precision, train_recall, \
                  test_accuracy, test_precision, test_recall))    
                  
            avg_train_acc += train_accuracy
            avg_train_pre += train_precision
            avg_train_rec += train_recall
            avg_test_acc  += test_accuracy
            avg_test_pre  += test_precision
            avg_test_rec  += test_recall
            cv_num+=1
        print('| avg  |  {:0.4f}   |  {:0.4f}   |  {:0.4f}  |  {:0.4f}   |  {:0.4f}   |  {:0.4f}   |'.format(\
                avg_train_acc/CV, avg_train_pre/CV, avg_train_rec/CV, \
                avg_test_acc/CV, avg_test_pre/CV, avg_test_rec/CV ))         

        print("testing...\r", end = "")
        y_predict = svm_model.predict(standard_scaler.transform(x_test))
        accuracy = metrics.accuracy_score(y_test, y_predict)
        precision = metrics.precision_score(y_test, y_predict, average='macro')
        recall = metrics.recall_score(y_test, y_predict, average='macro')
        
        print("Testing Result:")
        print("  Accuracy:",accuracy)
        print("  Precision:",precision)
        print("  Recall:",recall)
        
    else:
        print("-m(method) must be dct or svm")
        sys.exit()
        
    
