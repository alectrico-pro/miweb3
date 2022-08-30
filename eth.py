#!/usr/bin/env python
#https://web3py.readthedocs.io/en/latest/quickstart.html
from web3 import Web3, EthereumTesterProvider
w3= Web3( EthereumTesterProvider() )
print(w3.isConnected())

print(w3.eth.get_block('latest'))
