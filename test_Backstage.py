# -*- coding: utf-8 -*-
from gilded_rose_refactorizado_test import *

if __name__ == '__main__':

    item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 20):
        item.update_quality()
        print(item)

    itemInterfaz = Interfaz()
    itemInterfaz.update_quality()
