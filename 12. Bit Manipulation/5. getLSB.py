"""
This will give u the lsb of any number u pass

"""


def getLSB(num):

    return num & ~(num - 1)