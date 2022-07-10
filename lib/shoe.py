#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self, brand):
        pass
        self.brand = brand

    def get_color(self):
        pass
        return self._color

    def set_color(self, color):
        pass
        self._color = color

    def get_size(self):
        pass
        return self._size

    def set_size(self, size):
        pass
        self._size = size

    def get_material(self):
        pass
        return self._material

    def set_material(self, material):
        pass
        self._material = material

    def get_condition(self):
        pass
        return self._condition

    def set_condition(self, condition):
        pass
        self._condition = condition

    color = property(get_color, set_color)
    size = property(get_size, set_size)
    material = property(get_material, set_material)
    condition = property(get_condition, set_condition)

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")