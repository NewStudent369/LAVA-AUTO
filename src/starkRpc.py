
import requests
import random
import time
from datetime import datetime
urlMain = 'https://rpc.starknet.lava.build/lava-referer-4868f752-abbc-4f16-8c7e-fabad2cc33f2/'
urlTest = 'https://rpc.starknet-testnet.lava.build/lava-referer-71e009b6-97d4-4ed1-a5ad-d874e2609e25/'
starknet_chainId = {
    "jsonrpc":"2.0",
    "method":"starknet_chainId",
    "params":[],
    "id":0
}

starknet_getClassHashAt = {
    "jsonrpc":"2.0",
    "method":"starknet_getClassHashAt",
    "id":1
}

starknet_pendingTransactions = {
    "jsonrpc":"2.0",
    "method":"starknet_getPendingTransactions",
    "id":1
}

starknet_blockNumber= {
    "jsonrpc":"2.0",
    "method":"starknet_blockNumber",
    "id":1
}

starknet_getTransactionByHash= {
    "jsonrpc":"2.0",
    "method":"starknet_getTransactionByHash",
    "params":['0x019041241b3e0924636b94fd780eca8ed82149299a5fd2f9c90aaeabe5da8728'],
    "id":1
}





while True:
    try:
        a=requests.post(url=urlMain,json=starknet_chainId)
        t11=random.randint(1,5)
        time.sleep(t11)
        #b=requests.post(url=urlMain,json=starknet_getClassHashAt)
        #d=requests.post(url=urlMain,json=starknet_blockNumber)
        e=requests.post(url=urlMain,json=starknet_getTransactionByHash)
        t1=random.randint(10,20)
        time.sleep(t1)
        a=requests.post(url=urlTest,json=starknet_chainId)
        #b=requests.post(url=urlTest,json=starknet_getClassHashAt)
        #d=requests.post(url=urlTest,json=starknet_blockNumber)
        t21=random.randint(1,5)
        time.sleep(t21)
        e=requests.post(url=urlTest,json=starknet_getTransactionByHash)
        t2=random.randint(10,20)
        time.sleep(t2)
        print("休息%d秒"%(t1+t2+t11+t21,))
    except:
        print(str(datetime.now())+"休息%180秒")
        time.sleep(180)


