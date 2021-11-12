from brownie import PancakeFactory, Contract
from .helpful_scripts import get_account

def main():
  account = get_account()
  factory = Contract.from_abi("PancakeFactory", "0xf96460E81015714EC57c3993147aea0F7B8CBDFf", PancakeFactory.abi)
  tx = factory.createPair("0x61505879BB49caf3fDCb9A3148B75093509Ffc80" ,"0xae13d989daC2f0dEbFf460aC112a837C89BAa7cd", {"from": account})
  tx.wait(1)

  print(f'{tx.logs}')