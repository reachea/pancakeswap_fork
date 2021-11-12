from brownie import PancakeRouter, config, network
from .helpful_scripts import get_account

FACTORY_ADDRESS = "0x55D1C68af3e8652455073fe26FF84D9914580Acf"
WBNB_ADDRESS = "0xae13d989dac2f0debff460ac112a837c89baa7cd"

def main():
  account = get_account()
  uniswap_router = deploy_factory(account)


def deploy_factory(account):
  uniswap_router = PancakeRouter.deploy(FACTORY_ADDRESS, WBNB_ADDRESS, {"from": account}, publish_source=config["wallets"][network.show_active()].get("verify"))
  print(f'Factory Contract Deployed in {uniswap_router.address}')
  return uniswap_router.address