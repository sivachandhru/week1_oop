import pytest
from bank import BankAccount

def test_deposit_and_balance():
    a = BankAccount("A")
    a.deposit(100.0)
    assert a.balance() == 100.0

def test_withdraw_ok():
    a = BankAccount("A", 50.0)
    a.withdraw(20.0)
    assert a.balance() == 30.0

def test_withdraw_insufficient():
    a = BankAccount("A", 10.0)
    with pytest.raises(ValueError):
        a.withdraw(20.0)

def test_transfer_ok():
    a = BankAccount("A", 100.0); b = BankAccount("B", 10.0)
    a.transfer(b, 40.0)
    assert a.balance() == 60.0 and b.balance() == 50.0

@pytest.mark.parametrize("amt", [0.0, -5.0])
def test_transfer_invalid_amounts(amt):
    a = BankAccount("A", 100.0); b = BankAccount("B", 0.0)
    with pytest.raises(ValueError):
        a.transfer(b, amt)
