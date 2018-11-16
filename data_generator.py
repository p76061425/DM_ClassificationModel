import numpy as np
import argparse
import re
import sys
import os

def save_data(file_name,data):

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
        for i in range(data_amount):
            f.write("\n" + str(house_value[i])+" "+str(car_value[i])+" "+str(land_value[i])+" "+\
                    str(income_value[i])+" "+str(mate_value[i])+" "+str(int(class_vlaue[i])))    

                    
def gen_data(data_amount):                     
    house_value = np.random.randint(0, 5, data_amount)
    car_value = np.random.randint(0, 5, data_amount)
    land_value = np.random.randint(0, 5, data_amount)
    income_value = np.random.randint(-50000, 100000, data_amount)
    mate_value = np.random.randint(0,2 , data_amount) 
    class_vlaue = np.zeros([data_amount,])    
    for i in range(data_amount):
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
 
    parser.add_argument('-n',
                        default="10000",
                        dest='DATA_AMOUNT',
                        help='The number of data you want to generate, default = 10000')
    args = parser.parse_args()
    
    train_data_file_nmae = "train_data.txt" 
    test_data_file_nmae = "test_data.txt" 
    
    #attributes_list = ["house","car","land","income","mate","class",]
    data_amount = int(args.DATA_AMOUNT)
    
    train_data = gen_data(data_amount)
    save_data(train_data_file_nmae,train_data)
    
    test_data = gen_data(data_amount)
    save_data(test_data_file_nmae,test_data)
    


    
    
    