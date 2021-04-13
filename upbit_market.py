#Upbit 종목 선택, 종목에 대한 데이터 추출
import requests
import datetime
import pandas as pd
import json
import re
import time
import os

def Choose_coin(coin_list = None):
    """
    KRW-coin의 종목을 korean, english를 dic형태로 반환
    coin_list에는 korean KRW-coin을 리스트형태로 지정해주어야 한다.
    None인 경우 KRW-coin전체를 반환
    """
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails":"false"}
    response = requests.request("GET", url, params=querystring)
    contents = response.json()
    KRW_coin_dic = {}

    for x in contents:
        if "KRW" in x['market']:
            KRW_coin_dic[str(x['market'])] = x['korean_name']
    if coin_list is not None:
        for key, value in list(KRW_coin_dic.items()):
            if value not in coin_list:
                del(KRW_coin_dic[str(key)])
        return KRW_coin_dic
    else:
        return KRW_coin_dic


def get_url_ohlcv(interval):
    """
    candle에 대한 요청 주소를 얻는 함수
    :param interval: day(일봉), minute(분봉), week(주봉), 월봉(month)
    :return: candle 조회에 사용되는 url
    """
    if interval in ["day", "days"]:
        url = "https://api.upbit.com/v1/candles/days"
    elif interval in ["minute1", "minutes1"]:
        url = "https://api.upbit.com/v1/candles/minutes/1"
    elif interval in ["minute3", "minutes3"]:
        url = "https://api.upbit.com/v1/candles/minutes/3"
    elif interval in ["minute5", "minutes5"]:
        url = "https://api.upbit.com/v1/candles/minutes/5"
    elif interval in ["minute10", "minutes10"]:
        url = "https://api.upbit.com/v1/candles/minutes/10"
    elif interval in ["minute15", "minutes15"]:
        url = "https://api.upbit.com/v1/candles/minutes/15"
    elif interval in ["minute30", "minutes30"]:
        url = "https://api.upbit.com/v1/candles/minutes/30"
    elif interval in ["minute60", "minutes60"]:
        url = "https://api.upbit.com/v1/candles/minutes/60"
    elif interval in ["minute240", "minutes240"]:
        url = "https://api.upbit.com/v1/candles/minutes/240"
    elif interval in ["week",  "weeks"]:
        url = "https://api.upbit.com/v1/candles/weeks"
    elif interval in ["month", "months"]:
        url = "https://api.upbit.com/v1/candles/months"
    else:
        url = "https://api.upbit.com/v1/candles/days"
    return url


def get_coin_data(local_path = None, coin_list = None):
    """
    coin_list에 대해 전체 데이터 1day간격 데이터를 추출
    local_path의 data폴더에 저장
    """
    KRW_coin_dic = Choose_coin(coin_list = coin_list)
    count = 200
    for market in KRW_coin_dic.keys():
        df = pd.DataFrame()
        date_now =  datetime.datetime.now()
        for i in range(0, 40001, count):
            date = (date_now - datetime.timedelta(hours= i * 24 + 9*60)).strftime('%Y-%m-%d %H:%M:%S')
            querystring = {"market":market, "to":date, "count":str(count)} #UTC
            response = requests.request("GET", get_url_ohlcv("days"), params=querystring)
            contents = response.json()
            dt_list = [datetime.datetime.strptime(x['candle_date_time_kst'], "%Y-%m-%dT%H:%M:%S") for x in contents]
            df = pd.concat([df, pd.DataFrame(contents, columns=['opening_price', 'high_price', 'low_price', 'trade_price', 'candle_acc_trade_volume'], index=dt_list)])
            time.sleep(0.1005)
            print("load data: " + market + "  " + str(int(i/200)) + " / " + "200")            
            df[::-1].to_csv(os.path.join(local_path,'data',market + '.csv'), mode='w')
    return KRW_coin_dic