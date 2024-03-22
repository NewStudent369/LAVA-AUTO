
import requests
import random
import time
urlMain = 'https://tm.axelar.lava.build/lava-referer-71e009b6-97d4-4ed1-a5ad-d874e2609e25/'
urlTest = 'https://tm.axelar-testnet.lava.build/lava-referer-71e009b6-97d4-4ed1-a5ad-d874e2609e25/'

account={
  "jsonrpc": "2.0",
  "id": "1",
  "method": "status",
  "params": []
}
account={
  "jsonrpc": "2.0",
  "id": "1",
  "method": "status",
  "params": []
}

account1={
  "jsonrpc": "2.0",
  "id": "1",
  "method": "params",
  "params": []
}


api=r'axelar/nexus/v1beta1/params'

while True:
    try:
        #aa=requests.get(url=urlMain+api)
        a=requests.post(url=urlMain, json=account)
        t2=random.randint(10,30)
        b=requests.post(url=urlTest,json=account)
        t2=random.randint(10,30)
        time.sleep(t2)
        print("休息%d秒"%(t2,))
    except:
        time.sleep(180)
        print("休息180秒")
    #c=requests.post(url=urlMain,json=block)




