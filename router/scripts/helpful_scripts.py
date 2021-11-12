from brownie import accounts, config, network

DEVELOPMENT_NETWORKS = ["development"]

def get_account(index=None):
  if (network.show_active() in DEVELOPMENT_NETWORKS):
    if (index != None):
      return accounts[index]
    else:
      return accounts[0]
  else:
    return accounts.add(config["wallets"][network.show_active()]["account"])
