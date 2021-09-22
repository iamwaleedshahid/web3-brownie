from lib2to3.pgen2.literals import simple_escapes
from tracemalloc import start
from brownie import SimpleStorage, accounts


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    starting_value = simple_storage.retrieve()

    expected_value = 0

    assert starting_value == expected_value


def test_updating_storage():
    #Arrange
    account = accounts[0]

    simple_storage = SimpleStorage.deploy({"from": account})

    #Act
    expected_value = 222
    simple_storage.store(expected_value, {"from": account})

    #Assert
    assert expected_value == simple_storage.retrieve()