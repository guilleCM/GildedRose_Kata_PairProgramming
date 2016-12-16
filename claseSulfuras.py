class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)	

        
    def update_quality(self):
        assert self.quality == 80, "Quality de %s no es 80" % self.__class__.__name__
        pass
