import numpy as np
import argparse
import re
import sys
import os

def save_data(file_name,data,data_size):

    house_value = data[0]
    car_value = data[1]
    land_value = data[2]
    income_value = data[3]
    mate_value = data[4]
    class_vlaue = data[5]
    
    data_dir = "./data/"
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)

    with open(data_dir+file_name, 'w') as f:
        f.writelines("house car land income mate class")
        for i in range(data_size):
            f.write("\n" + str(house_value[i])+" "+str(car_value[i])+" "+str(land_value[i])+" "+\
                    str(income_value[i])+" "+str(mate_value[i])+" "+str(int(class_vlaue[i])))    

                    
def gen_data(data_size):                     
    house_value = np.random.randint(0, 5, data_size)
    car_value = np.random.randint(0, 5, data_size)
    land_value = np.random.randint(0, 5, data_size)
    income_value = np.random.randint(-50000, 100000, data_size)
    mate_value = np.random.randint(0,2 , data_size) 
    class_vlaue = np.zeros([data_size,])    
    for i in range(data_size):
        if( house_value[i]>=3 ):
            if(land_value[i]>=3):
                if(mate_value[i]==1):
                    class_vlaue[i] = 3
                else:
                    class_vlaue[i] = 2
            elif(car_value[i]>=3):
                if(mate_value[i]==1):
                    class_vlaue[i] = 3
                else:
                    class_vlaue[i] = 2
            else:
                class_vlaue[i] = 1
        else:
            if(income_value[i] >= 40000):
                if(mate_value[i]==1):
                    class_vlaue[i] = 1
                else:
                    class_vlaue[i] = 0
            else:
                class_vlaue[i] = 0
            
    return [house_value,car_value,land_value,income_value,mate_value,class_vlaue]
    
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
 
    parser.add_argument('-train',
                        default="10000",
                        dest='TRAIN_SIZE',
                        help='The number of training data you want to generate, default = 10000')
    parser.add_argument('-test',
                        default="10000",
                        dest='TEST_SIZE',
                        help='The number of testing data you want to generate, default = 10000')                        
    args = parser.parse_args()
    
    train_data_file_nmae = "train_data.txt" 
    test_data_file_nmae = "test_data.txt" 
    
    #attributes_list = ["house","car","land","income","mate","class",]
    train_size = int(args.TRAIN_SIZE)
    test_size = int(args.TEST_SIZE)
    
    train_data = gen_data(train_size)
    save_data(train_data_file_nmae,train_data,train_size)
    
    test_data = gen_data(test_size)
    save_data(test_data_file_nmae,test_data,test_size)
    


    
    
    