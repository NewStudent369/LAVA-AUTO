
import requests
import random
import time
urlMain = 'https://near.lava.build/lava-referer-71e009b6-97d4-4ed1-a5ad-d874e2609e25/'
urlTest = 'https://near-testnet.lava.build/lava-referer-71e009b6-97d4-4ed1-a5ad-d874e2609e25/'

account={
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "query",
  "params": {
    "request_type": "view_account",
    "finality": "final",
    "account_id": "919133682.near"
  }
}

gas={
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "gas_price",
  "params": [None]
}

block={
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "block",
  "params": {
    "finality": "final"
  }
}






while True:
    try:
        a=requests.post(url=urlMain,json=account)
        t2=random.randint(10,30)
        b=requests.post(url=urlMain,json=gas)
        t2=random.randint(10,30)
        time.sleep(t2)
        print("休息%d秒"%(t2,))
    except:
        time.sleep(180)
        print("休息180秒")
    #c=requests.post(url=urlMain,json=block)




