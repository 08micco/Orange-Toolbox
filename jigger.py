import logging
import string
import random

vocals = {"a", "e", "i", "o", "u", "y", "æ", "ø", "å"}


class Jigger:
    def jig(level, address, house_num, amount):
        addresses = {}
        for x in range(amount):
            addresses[x] = address + " " + house_num
        # for x in range(amount):
        # addresses[x] = Jigger.double_vocal(addresses[x])
        for x in range(amount):
            addresses[x] = Jigger.three_letter(addresses[x])
        Jigger.print_addressess(addresses)

    def three_letter(address):
        x1 = random.choice(string.ascii_letters).upper()
        x2 = random.choice(string.ascii_letters).upper()
        x3 = random.choice(string.ascii_letters).upper()
        return x1 + x2 + x3 + " " + address

    """
    def double_vocal(address):
        ran = random.randint(0, 8)
        print(ran)
        x = str(vocals[ran])
        for x in vocals:
            print(x)
            if x in address:
                address_split = address.split(x)
                return address_split[0] + x + x + address_split[1]
            else:
                return address
                """

    def print_addressess(addresses):
        for x in addresses:
            print(addresses[x])


def main(level, address, house_num, amount):

    Jigger.jig(level, address, house_num, amount)
