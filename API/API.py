import json
from web3 import Web3
from solcx import compile_standard, install_solc
import codecs
from os.path import exists
import os
import hashlib

class Web3DatabaseAPI:

    def ini(self, reset):
        if reset and exists("./contract_address.txt"):
            os.remove("./contract_address.txt")

        self.web3 = Web3(Web3.HTTPProvider(self.node_url))
        self.chain_id = 5

        compiled_sol = self.sol_2_json()
        self.abi = self.get_abi(compiled_sol)
        self.bytecode = self.get_bytecode(compiled_sol)

        acct = self.web3.eth.account.privateKeyToAccount(self.private_key)
        self.account_address = acct.address

        if not(exists("./contract_address.txt")):
            self.deploy()
            with open("./contract_address.txt", 'w') as f:
                f.write(self.contract_address)
        else:
            with open("./contract_address.txt", 'r') as f:
                self.contract_address = f.read()
                self.update_contract()

    def __init__(self,node_url,private_key,reset=False):
        self.node_url = node_url
        self.contract_address = ""
        self.private_key = private_key
        self.ini(reset)
    
    def deploy(self):
        contract = self.web3.eth.contract(abi = self.abi, bytecode = self.bytecode)

        nonce = self.web3.eth.getTransactionCount(self.account_address)

        transaction = contract.constructor().buildTransaction(
            {
                "chainId": self.chain_id,
                "gasPrice": self.web3.eth.gas_price,
                "from": self.account_address,
                "nonce": nonce,
            }
        )

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        print("Deploying Contract!")

        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        print("Waiting for transaction to finish...")
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

        self.contract_address = tx_receipt.contractAddress
        self.update_contract()

    def update_contract(self):
        self.contract = self.web3.eth.contract(address=self.contract_address, abi = self.abi)
        self.contract_instance = self.web3.eth.contract(abi=self.abi, address=self.contract_address)

    def hash(key):
        v = hashlib.sha256(key.encode()).hexdigest()
        return int(v,base=16)

    def get(self,key):

        a = self.contract.functions.get(key).call()

        return a

    def set(self,key,value):

        tx = self.contract_instance.functions.set(key, value).buildTransaction(
            {'nonce': self.web3.eth.getTransactionCount(self.account_address)})

        signed_tx = self.web3.eth.account.signTransaction(tx, self.private_key)

        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        self.web3.eth.wait_for_transaction_receipt(tx_hash.hex())

        print(tx_hash.hex())
        print(self.private_key)

    def sol_2_json(self):
        sol_version = "0.8.7"
        sol_path = "./storage.sol"
        json_path = "./storage.json"

        if not(exists(json_path)):
            with open(sol_path, "r") as file:
                storage_file = file.read()
            install_solc(sol_version)

            compiled_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {sol_path: {"content": storage_file}},
                "settings": {
                    "outputSelection": {
                        "*": {
                            "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                        }
                    }
                },
            },
            solc_version=sol_version,
            )

            with open(json_path, "w") as file:
                json.dump(compiled_sol, file)

        else:
            with open(json_path, "r") as file:
                compiled_sol = json.load(file)

        return compiled_sol

    def get_abi(self,compiled_sol):
        abi = json.loads(
            compiled_sol["contracts"]["./storage.sol"]["Storage"]["metadata"]
        )["output"]["abi"]

        return abi

    def get_bytecode(self, compiled_sol):
        bytecode = compiled_sol["contracts"]["./storage.sol"]["Storage"]["evm"][
            "bytecode"
        ]["object"]

        return bytecode
