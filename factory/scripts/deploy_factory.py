from brownie import PancakeFactory, config, network
from .helpful_scripts import get_account

def main():
  account = get_account()
  uniswap_factory = deploy_factory(account)


def deploy_factory(account):
  uniswap_factory = PancakeFactory.deploy(account, {"from": account}, publish_source=config["wallets"][network.show_active()].get("verify"))
  print(f'Factory Contract Deployed in {uniswap_factory.address}')
  return uniswap_factory.address