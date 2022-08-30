#!/usr/bin/env python
#https://web3py.readthedocs.io/en/latest/quickstart.html
from web3 import Web3, EthereumTesterProvider
from solcx import install_solc
install_solc(version='latest')

from solcx import compile_source

w3= Web3( EthereumTesterProvider() )
print(w3.isConnected())

print(w3.eth.get_block('latest'))


compiled_sol = compile_source(
    '''
     pragma solidity >0.5.0;

     contract Greeter {
         string public greeting;

         constructor() public {
            greeting = 'Hello';
         }

        function setGreeting(string memory _greeting) public {
             greeting = _greeting;
        }

        function greet() view public returns (string memory) {
            return greeting;
         }
     }
     ''',
    output_values=['abi', 'bin']
)

print( "#compiled_sol" )
print( compiled_sol )


contract_id, contract_interface = compiled_sol.popitem()
print( "#contract_id" )
print( contract_id)

print( "#contract_interface" )
print( contract_interface)

print("#bytecode")
bytecode = contract_interface['bin']
print( bytecode )

print("#abi" )
abi = contract_interface['abi']
print( abi )

print( "#w3")
w3 = Web3(Web3.EthereumTesterProvider())
print( w3) 

print( "# set pre-funded account as sender ")
w3.eth.default_account = w3.eth.accounts[0]

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

print( "# Submit the transaction that deploys the contract")
tx_hash = Greeter.constructor().transact()

print( "# Wait for the transaction to be mined, and get the transaction receipt" )
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract( address=tx_receipt.contractAddress, abi=abi )

greeter.functions.greet().call() 

tx_hash     = greeter.functions.setGreeting('Nihao').transact()
tx_receipt  = w3.eth.wait_for_transaction_receipt(tx_hash)
greeter.functions.greet().call() 
