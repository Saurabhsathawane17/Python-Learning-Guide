"""OOPS PROJECT BASED ON INHERITANCE"""

class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__ (self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(Factory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips)
        self.pockets = pockets

obj = BhopalFactory("leather", 5, "black")