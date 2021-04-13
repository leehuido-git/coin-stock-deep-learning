'''
upbit_main.py
#추출한 데이터를 통해 LSTM 학습
#data 폴더안에 있는 모든 csv 학습
Author: Huido Lee (j3jjj2021@naver.com)
'''
import os
from upbit_market import get_coin_data
from upbit_deep import coin_train
from upbit_deep_test import coin_predict

if __name__ == '__main__':
    local_path = os.getcwd()
    coin_list_path = os.path.join(local_path, "coin_list.txt")
    if os.path.isfile(coin_list_path) is False:
        exit('coin_list.txt file does not exist.')
    f = open(coin_list_path, 'r', encoding='UTF8')
    lines = f.readlines()
    coin_list = []
    for line in lines:
        for coin in line.split():
            coin_list.append(coin)
    f.close()

    get_coin_data(local_path = local_path, coin_list= coin_list)    
    coin_train(local_path = local_path, coin_list= coin_list)
    coin_predict(local_path= local_path, coin_list= coin_list)