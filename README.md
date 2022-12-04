# Tenderly_Hackathon_2022

## General Info
Layer between user python code and the blockchain that provides an API for automatized and transparent data storaging and communication with the blockchain. 

## Usage and Motivation
The goal is to remove the need for services that web3 storage providers offer and decentralize communication with the blockchain and make it transparent for users that don't know much about Web3 technologies.

## Features
This program implements features for:
* Automatized smart contract deployment
* Storing data in (key, value) format
* Reading data by passing key value

## How To Use
* Transfer Goerli funds to your wallet using this [link](https://goerlifaucet.com/) 
* Create Infura account and get Goerli link
* Get private key from your wallet
* Run following commands in your project terminal: <br/>
`git clone https://github.com/strajdzsha/Tenderly_Hackathon_2022` <br/>
`cd Tenderly_Hackathon_2022` <br/>
`pip install -e .  `
* Import class Web3DatabaseAPI
* Create object of type Web3DatabaseAPI and pass Goerli link and private key as constructor parameters

## Example
```python
from API.API import Web3DatabaseAPI

infura_url = "https://goerli.infura.io/v3/YOUR-API-KEY"
private_key = "<Private key with 0x prefix>"

obj = Web3DatabaseAPI(infura_url, private_key)

obj.set(123,"message")
msg = obj.get(123)
print(msg)
obj.set(333, "poruka2")
msg = obj.get(333)
print(msg)
