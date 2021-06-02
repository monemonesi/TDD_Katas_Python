import pytest
import random
import SalesByMatch as Seller


def test_sock_merchant_should_return_zero_when_no_socks() -> None:
    """The number of pairs in an empty list is should be 0"""
    assert Seller.sock_merchant(0, []) == 0


def test_sock_merchant_should_return_zero_with_only_one_sock() -> None:
    """The number of pairs in a list with only one value should be 0"""
    assert Seller.sock_merchant(1, [random.randint(0, 100)]) == 0


@pytest.mark.parametrize("sock", [random.randrange(0, 100)])
def test_sock_merchant_should_return_zero_with_only_different_socks(sock: int) -> None:
    """The number of pairs should be one when two socks of the same colour are given"""
    assert Seller.sock_merchant(2, [sock, sock+1, sock-1, sock+10]) == 0


@pytest.mark.parametrize("sock", [random.randrange(0, 100)])
def test_sock_merchant_should_return_one_with_a_pair_of_socks(sock: int) -> None:
    """The number of pairs should be one when two socks of the same colour are given"""
    assert Seller.sock_merchant(2, [sock, sock]) == 1


@pytest.mark.parametrize("sock", [random.randrange(0, 100)])
def test_sock_merchant_should_return_one_with_a_pair_of_socks_and_one_odd(sock: int) -> None:
    """The number of pairs should be one when two socks of the same colour are given"""
    assert Seller.sock_merchant(3, [sock, sock, sock+1]) == 1


@pytest.mark.parametrize("sock", [random.randrange(0, 100)])
def test_sock_merchant_should_return_two_with_two_pair_of_socks(sock: int) -> None:
    """The number of pairs should be one when two socks of the same colour are given"""
    assert Seller.sock_merchant(3, [sock, sock, sock+1, sock+1, sock+2]) == 2