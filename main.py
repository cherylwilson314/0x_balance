#check EVM balance
from web3 import Web3

#RPC
sepolia_url ='https://rpc.sepolia.org'

#Connection
web3 = Web3(Web3.HTTPProvider(sepolia_url))
print('connection', web3.is_connected())

#check balance
file = open('wallet.txt')
total = 0
stt = 0
for line in file:
    balance = web3.eth.get_balance(line.strip())
    eth = web3.from_wei(balance,'ether')
    tx_count = web3.eth.get_transaction_count(line.strip())

    print(f'Wallet {stt}:', round(eth, 4),'ETH ----', tx_count, "transactions")
    total += eth
    stt += 1

#print total balance
print('total =', round(total, 4), "ETH")
