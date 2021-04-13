# coin-stock-deep-learning
upbit-api를 통해서 coin 데이터를 받아 LSTM으로 주가 예측

## 개요
본 시스템은 크게 3가지 단계로 이루어져 있습니다.
1. Data pre-processing
upbit-api를 통해서 원하는 코인의 'opening_price', 'high_price', 'low_price', 'trade_price', 'candle_acc_trade_volume'를 가져와 .csv로 저장합니다.
2. Deep learning
데이터를 LSTM을 통해 학습합니다.
3. Predict
학습한 모델을 통해서 하루 뒤의 코인 주가를 예측합니다.

## Installation
파이썬 개발 환경으로 최신 버전의 Anaconda를 설치하세요. (Python3 버전용)
* tensorflow (2 이상)
* pandas
* numpy
* scikit-learn
* matplotlib
* tqdm
* requests

```
$ pip install -r requirements.txt
```

필수 디렉토리는 다음과 같습니다:
```
.
├── coin_list.txt
├── upbit_main.py
├── upbit_market.py
├── upbit_deep.py
├── upbit_deep_test.py
├── checkpoint/
└── data/
```

각각의 것들에 대한 개요입니다:

| 파일 | 설명 |
| -------- | ----------- |
| `coin_list.txt` | 원하는 코인이름 입력 |
| `upbit_main.py` | main |
| `upbit_market.py` | coin-stock데이터 받아오기 |
| `upbit_deep.py` | deep learning학습 |
| `upbit_deep_test.py` | 검증 |

시작하기 앞서 coin_list.txt에 원하는 코인의 이름을 **한글명**으로 적어야합니다
```
비트코인 이더리움
리플 에이다
폴카닷
```

다음과 같이 프로그램을 실행 합니다
```
$ python upbit_main.py
```

결과는 아래의 파일과 같이 저장됩니다
1. coin stock data: (./data/**coin name**.csv)
2. loss: (./**coin name**.png)
3. checkpoint (./checkpoint/**coin name**.ckpt)
4. result (./**coin name**_pred.png)
**1. coin stock data**
![data](./img/data.png)

**2. loss**
![loss](./img/loss.png)

**4. result**
![result](./img/result.png)
