# -*- coding: utf-8 -*-
from gilded_rose_refactorizado_test import *

if __name__ == '__main__':

    item = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

    itemInterfaz = Interfaz()
    itemInterfaz.update_quality()
