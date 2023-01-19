from brownie import SimpleStorage, config, accounts


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


# Private key: 41ac779a5b240793bb26c14356ced5d7a75b06ad981fcc736af56a9b21a7ca3f


def main():
    deploy_simple_storage()
