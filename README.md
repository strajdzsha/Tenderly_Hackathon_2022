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
* Create Infura account and get Goerli link
* Get private key from your wallet
* Run following commands in your project terminal: <br/>
`git clone https://github.com/strajdzsha/Tenderly_Hackathon_2022  
cd Tenderly_Hackathon_2022  
pip install -e .  `
* Import class Web3DatabaseAPI
* Create object of type Web3DatabaseAPI and pass Goerli link and private key as constructor parameters

## Example
```python
from API import Web3DatabaseAPI

infura_url = "https://goerli.infura.io/v3/404781d45d67498e91fbf60644a7cbbb"
private_key = "0x67ef89d575d630955faa22deabf035e756eaf6445221566090f7acc7ceb8f261"

obj = Web3DatabaseAPI(infura_url, private_key)

obj.set(123,"message")
msg = obj.get(123)
print(msg)
