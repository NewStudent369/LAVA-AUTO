import os

import ecdsa
import time
from ecdsa import SECP256k1
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
from web3 import Web3,HTTPProvider
import random
pth=os.getcwd()
wltPth=os.path.join(pth,'wallet')
outfileId=os.path.join(wltPth,'walletId')
outfileName=os.path.join(wltPth,'walletPrice')

def isGoodWallet(walletId):
    strWallet=str(walletId)
    if strWallet.find('88888888') >= 0 or strWallet.find('11111111') >= 0 or strWallet.find('22222222') >= 0 or strWallet.find('33333333') >= 0 or \
        strWallet.find('44444444') >= 0 or \
        strWallet.find('55555555') >= 0 or \
        strWallet.find('66666666') >= 0 or \
        strWallet.find('77777777') >= 0 or \
        strWallet.find('88888888') >= 0 or \
        strWallet.find('99999999') >= 0 or \
        strWallet.find('00000000') >= 0 :
        return True
    else:
        return False



def work():
    while True:
        try:
            web32 = Web3(HTTPProvider('https://eth1.lava.build/lava-referer-71e009b6-97d4-4ed1-a5ad-d874e2609e25/'))
            # web3 = Web3(HTTPProvider('https://eth1.lava.build/lava-referer-71e009b6-97d4-4ed1-a5ad-d874e2609e25/'))

            while True:
                privateKey = ecdsa.SigningKey.generate(curve=SECP256k1).to_string()
                privateKeyStr = privateKey.hex()
                hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
                hdwallet.from_private_key(private_key=privateKeyStr)
                priv = hdwallet.private_key()
                addr = hdwallet.p2pkh_address()
                price = web32.eth.getBalance(addr)
                price1 = web32.eth.getBalance('0xe1de9179fc0D13f80D3458a29193DC58bb4f9bdf')
                print(priv + ' ' + addr + ":" + str(price))
                count = addr.count('0')
                length = len(set(list(addr)))

                a=random.randint(20,60)
                if isGoodWallet(addr):
                    fpId = open(outfileId, 'a+')
                    print(priv + ' ' + addr + ":" + str(price))
                    fpId.write(priv + ' ' + addr + ' ' + str(price) + '\n')
                    fpId.close()
                if int(price) > 0 or count > 30 or length < 10:
                    fpprice = open(outfileName, 'a+')
                    print(priv + ' ' + addr + ":" + str(price))
                    fpprice.write(priv + ' ' + addr +' '+ str(price)+'\n')
                    fpprice.close()
                    time.sleep(0.5)
                print("休息%sS继续" % (a,))
                time.sleep(a)

                # price2 = web32.eth.getBalance(addr)
                # price3 = web33.eth.getBalance(addr)
        except:
            print('链接错误,休息2分钟')
            time.sleep(300)

if __name__ == '__main__':
    work()

