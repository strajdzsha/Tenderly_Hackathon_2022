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
todo..

## Example
```python
from Web3DatabaseAPI import Web3DatabaseAPI

obj = Web3DatabaseAPI()

obj.set(123,"message")
msg = obj.get(123)
print(msg)
```
