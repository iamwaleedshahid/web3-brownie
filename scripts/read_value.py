# Reading value from a deployed contract
from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1] #Pull the latest one

    print(simple_storage.retrieve())


def main():
    read_contract()