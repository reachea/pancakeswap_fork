from brownie import PancakeRouter, Contract, chain
from .helpful_scripts import get_account

def main():
  account = get_account()
  router = Contract.from_abi("PancakeRouter", "0x94040f8Bb736A7454623E141E515aC8683a6F5DA", PancakeRouter.abi)
  # weth = router.WETH()
  # factory = router.factory()

  # print(f'{chain.time()}')
  # print(f'{weth}')

  tx = router.addLiquidityETH(
    "0x61505879BB49caf3fDCb9A3148B75093509Ffc80",
    5000000000000000000000000000000,
    5000000000000000000000000000000,
    100000000000000000,
    "0x42Ba4d31Bb3aFc48af42F9603d3E1C860a2eBb22",
    chain.time(),
    {
      "from": account,
      "amount": 0.1,
    }
  )
  tx.wait(1)

  print(f'Transactions: {tx.logs}')