# coding: utf-8

"""
As its core, Python assert statement is a debugging aid that tests a condition.
"""


def apply_discount(product, discount):
    price = int(product['price'] * (1 - discount))
    assert 0 <= price <= product['price']
    return price

