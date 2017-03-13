# -*- coding: utf-8 -*-

from gilded_rose_refactorizado_test import *

class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
    	self.quality==80



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
