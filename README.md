# Data Mining Project 2
## P76061425 林聖軒

## Environment
* DISTRIB_ID=Ubuntu
* DISTRIB_RELEASE=18.04
* DISTRIB_CODENAME=bionic
* DISTRIB_DESCRIPTION=Ubuntu 18.04.1 LTS

# Usage
* Decision Tree
```sh
$ python3 decisionTree.py [-h] 
```
| optional Options | Description |
| ---              | --- |
| -h, --help       | show this help message and exit |
| -train, TRAIN_PATH    | Input training data file, default = ./data/train_data.txt |
| -test TEST_PATH  | Input testing data file, default = ./data/test_data.txt |

訓練decisionTree，並將訓練出的decisionTree結果output至當前目錄的tree.pdf中。</br>
需要安裝graphviz:
```sh
$ apt-get install graphviz
```


* **Data Generator**
```sh
$ python3 data_generator.py [-h]
```
| optional Options | Description |
| ---              | --- |
| -h, --help       | show this help message and exit |
| -n, DATA_AMOUNT  | The number of data you want to generate, default = 10000 |

執行後會在data資料夾內生成10000筆training data(train_data.txt)及testing data(test_data.txt)。


* **Absolutely Right Rules**

  * Attributes_list = house, car, land, income, mate, class 
  * house_value = [0, 5]
  * car_value = [0, 5]
  * land_value = [0, 5]
  * income_value = [-50000, 100000]
  * mate_value = [0, 1]
  * class_vlaue = {0, 1, 2, 3}


![](https://i.imgur.com/Pzdtmqs.png)


* **Decision tree**
  * Training size = 10000
  * Testing size = 10000
  * Criterion = Gini


![](https://i.imgur.com/6hgcwvx.png)

* **Result metrics**
  * Accuracy = 0.9997
  * Precision = 0.9999826689774697
  * Recall = 0.9999677377726158


* 從結果圖可以得知，與Absolutely Right Rules相比，Decision tree所建立出的model和實際的rules並非完全相同，但有很高的相似度，由於Absolutely Right Rules的規則很簡單，因此結果的Accuracy, Precision, Recall均有相當好的表現。